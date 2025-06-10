# Synchronizing group gameplay with TabletopKit

**Framework**: TabletopKit

Maintain game state across multiple players in a race to capture all the coins.

**Availability**:
- visionOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

This sample code project demonstrates how to overcome the difficult task of maintaining a multiplayer game’s state in real time. TabletopKit supports automatic game-state synchronization by keeping gameplay items, such as player tokens, dice, coins, and scenery updates — all with positions and actions — in sync during a multiplayer game. TabletopKit also supports many more gameplay styles than the traditional board game layout.

#### Set Up the App

The TabletopKit app object creates an instance of the `Game` class, which sets up, observes, and renders the [`TabletopGame`](tabletopgame.md) state. `Game` equipment, objects that implement the [`Equipment`](equipment.md) protocol, represents all interactive portions of a game. The `Game` class also handles game start and reset, initiating programmatic interactions, and adding equipment reset actions. The `GameSetup` class initializes and positions all game equipment.

The `GameRenderer` class implements [`TabletopGame.RenderDelegate`](tabletopgame/renderdelegate.md), which loads assets and communicates when the game needs visual updates. The `GameObserver` class implements [`TabletopGame.Observer`](tabletopgame/observer.md) and indicates confirmed gameplay actions. You can define custom actions to modify the game state to your needs. The `CustomAction.swift` file in this sample contains custom actions to reset the players, decrement player health, collect coins, reset coins, sink lily pads, and reset lily pads.

```swift
class Game {
    let tabletopGame: TabletopGame
    let renderer: GameRenderer
    let observer: GameObserver
    let setup: GameSetup

    //...
}
```

The `GameView` structure contains the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView), which hosts game content and the toolbar for player interaction, and stores the `Game` object as an environment property. The [`tabletopGame(_:parent:automaticUpdate:)`](https://developer.apple.com/documentation/SwiftUI/View/tabletopGame(_:parent:automaticUpdate:)) modifier connects the `TabletopGame` object to the `RealityView`. The modifier returns the appropriate delegate for the game equipment ID that passes into the update closure. A [`Task`](https://developer.apple.com/documentation/Swift/Task) creates `GroupActivityManager`, which connects multiple players and provides the `TabletopGame` object.

```swift
var body: some View {
    GeometryReader3D { proxy3D in
        RealityView { (content: inout RealityViewContent) in
            content.entities.append(volumetricRoot)
            // Set the root at the base of the volume.
            let frame = content.convert(proxy3D.frame(in: .local), from: .local, to: volumetricRoot)
            volumetricRoot.transform.translation.y = frame.min.y
            volumetricRoot.addChild(game.renderer.root)
        }
    }.toolbar() {
        GameToolbar(game: game)
    }.tabletopGame(game.tabletopGame, parent: game.renderer.root) { value in
        var delegate: GameInteraction?

        if let _ = game.tabletopGame.equipment(of: Log.self, matching: value.startingEquipmentID) {
            delegate = LogInteraction(game: game)
        } else if let _ = game.tabletopGame.equipment(of: LilyPad.self, matching: value.startingEquipmentID) {
            delegate = LilyPadInteraction(game: game)
        } else if let _ = game.tabletopGame.equipment(of: Player.self, matching: value.startingEquipmentID) {
            delegate = PlayerInteraction(game: game)
        } else {
            delegate = GameInteraction(game: game)
        }

        return delegate!
    }.task {
        activityManager = .init(tabletopGame: game.tabletopGame)
    }
}
```

The player joins other players by tapping the SharePlay button in the volume’s toolbar. This instantiates an `Activity` object that implements the [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity) protocol. `Activity` initializes an observable `GroupActivityManager` awaiting `Activity` sessions that coordinate with the provided `TabletopGame`. TabletopKit handles all player connections and synchronization. The app only needs to register its equipment and actions, and then handle their updates.

```swift
struct Activity: GroupActivity {
    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.type = .generic
        metadata.title = "TabletopKitSample"
        return metadata
    }
}

class GroupActivityManager: Observable {
    var tabletopGame: TabletopGame
    var sessionTask = Task<Void, Never> {}

    init(tabletopGame: TabletopGame) {
        self.tabletopGame = tabletopGame
        sessionTask = Task { @MainActor in
            for await session in Activity.sessions() {
                tabletopGame.coordinateWithSession(session)
            }
        }
    }

    deinit {
        tabletopGame.detachNetworkCoordinator()
    }
}
```

#### Define Gameplay

The game begins when the player taps the Start Game button in the toolbar. This sets the `Game.gameStarted` state to `true` and initiates `Log` entity interactions. Objects that implement the [`TabletopInteraction.Delegate`](tabletopinteraction/delegate.md) protocol handle all gameplay event updates.

```swift
class GameInteraction: TabletopInteraction.Delegate {
    let game: Game
    
    init(game: Game) {
        self.game = game
    }
    
    func update(interaction: TabletopKit.TabletopInteraction) {

    }
}
```

`PlayerInteraction` handles player input by implementing `TabletopInteraction.Delegate`. When the player gazes at a gameplay object and interacts using direct or indirect gestures, the `PlayerInteraction` receives a [`TabletopInteraction`](tabletopinteraction.md) object in its [`update(interaction:)`](tabletopinteraction/delegate/update(interaction:).md) method. TabletopKit supplies an active gesture for the interaction. The sample splits this functionality into two parts — updating based on user gestures and updating due to automatic programmatic interactions.

```swift
class PlayerInteraction: GameInteraction {
    override func update(interaction: TabletopInteraction) {
        // A gesture interaction to aim the jump.
        if interaction.value.gesture != nil || interaction.value.startingEquipmentID != interaction.value.controlledEquipmentID {
            updateGestureInteraction(interaction: interaction)
            return
        }
        
        // A programmatic interaction for the jump after the player releases the aim.
        updateProgrammaticInteraction(interaction: interaction)
    }
}
```

`PlayerInteraction` calls into `updateGestureInteraction` to handle gesture events. On gesture start, `updateGestureInteraction` sets the `.aimingSightID` for the controlled equipment on the interaction. This allows TabletopKit to manipulate the appropriate equipment entity onscreen.

```swift
func updateGestureInteraction(interaction: TabletopInteraction) {
    guard let gesture = interaction.value.gesture else { return }
    if gesture.phase == .started {
        guard let player = game.tabletopGame.equipment(matching: interaction.value.startingEquipmentID) as? Player else { return }
        interaction.setControlledEquipment(matching: .aimingSightID(for: player.seat))
        return
    }
    //...
```

On gesture update, `updateGestureInteraction` modifies the local slingshot visuals, matching user input.

```swift
    //...
    if gesture.phase == .update {
        // Update the slingshot visuals while the player is still dragging.
        game.tabletopGame.withCurrentSnapshot { snapshot in
            guard let (playerEquip, _) = snapshot.equipment(of: Player.self, matching: interaction.value.startingEquipmentID) else { return }
            let aimX = interaction.value.pose.position.x
            let aimZ = interaction.value.pose.position.z
            let root = game.renderer.root
            Task { @MainActor in
                playerEquip.updateAimingVisuals(dragPosition: .init(x: aimX, z: aimZ), root: root)
            }
        }
        return
    }
    //...
```

On gesture end, `updateGestureInteraction` calculates the change in gesture position, calls `TabletopKit/startInteraction(onEquipmentID:)` for the interaction’s equipment, and adds it to the programmatic player interaction dictionary of `Game`. When gesture handling is complete, TabletopKit moves the player’s piece.

```swift
    //...
    if gesture.phase == .ended {
        // When the player releases the aim, hide the aiming visuals and start a programmatic interaction for the jump.
        game.tabletopGame.withCurrentSnapshot { snapshot in
            if let (playerEquip, _) = snapshot.equipment(of: Player.self, matching: interaction.value.startingEquipmentID) {
                Task { @MainActor in
                    playerEquip.hideAimingVisuals()
                }
            }
            
            guard let interactionIdentifier = game.tabletopGame.startInteraction(onEquipmentID: interaction.value.startingEquipmentID) else {
                return
            }
            guard let (playerEquip, _) = snapshot.equipment(of: Player.self, matching: interaction.value.startingEquipmentID) else { return }
            
            let targetX = interaction.value.pose.position.x
            let targetZ = interaction.value.pose.position.z
            let root = game.renderer.root
            Task { @MainActor in
                game.programmaticPlayerInteractions[interactionIdentifier] = playerEquip.calcTargetPose(
                    dragPosition: .init(x: targetX, z: targetZ),
                    root: root
                )
                playerEquip.playJumpAudio()
            }
        }
        return
    }
}
```

Next, `PlayerInterction.updateProgrammaticInteraction` handles the programmatic interactions of automated equipment. At the beginning of the interaction, it provides the set of available interaction destinations — the stones, lily pads, and logs.

```swift
func updateProgrammaticInteraction(interaction: TabletopInteraction) {
    if interaction.value.phase == .started {
        interaction.setConfiguration(.init(allowedDestinations: .restricted(.allStones + .allLilyPads + .allLogs)))
        return
    }
    //...
```

During the interaction, the app finds a target programmatic player interaction for the provided interaction ID and sets the target’s position.

```swift
    //...
    if interaction.value.phase == .update {
        guard let targetPose = game.programmaticPlayerInteractions[interaction.value.id] else { return }
        let oldPose = interaction.value.pose
        
        if abs(oldPose.position.x - targetPose.position.x) < 1e-3 && abs(oldPose.position.z - targetPose.position.z) < 1e-3 {
            if interaction.value.proposedDestination == nil {
                sinkPlayer(interaction: interaction, targetPose: targetPose)
                return
            }
            interaction.setPose(targetPose)
            interaction.end()
            return
        }
        movePlayer(interaction: interaction, targetPose: targetPose)
        return
    }
    //...
```

At the end of the interaction, `updateProgrammaticInteraction` calls into `endJump`. Adding a [`MoveEquipmentAction`](moveequipmentaction.md) object to the active `TabletopInteraction` moves the player. If the target lands on a lily pad, the sample initiates the sinking animation by calling  `TabletopKit/startInteraction(onEquipmentID:)` with the lily pad’s equipment ID. If the target lands on an allowed destination with a coin, `endJump` adds a `CollectCoin` action to the active `TabletopInteraction`. The app then removes the interaction from the `programmaticPlayerInteractions` dictionary.

```swift
    //...
    if interaction.value.phase == .ended {
        endJump(interaction: interaction)
    }
}

func endJump(interaction: TabletopInteraction) {
    if let proposedDestination = interaction.value.proposedDestination {
        // Move the player to the proposed destination.
        interaction.addAction(.moveEquipment(matching: interaction.value.controlledEquipmentID,
                                             childOf: proposedDestination.equipmentID, pose: proposedDestination.pose))
        
        // If the destination is a lily pad, sink it.
        if game.tabletopGame.equipment(of: LilyPad.self, matching: proposedDestination.equipmentID) != nil {
            _ = game.tabletopGame.startInteraction(onEquipmentID: proposedDestination.equipmentID)
        }
        
        // If the destination contains an uncollected coin, collect it.
        game.tabletopGame.withCurrentSnapshot { snapshot in
            if let childId = snapshot.equipmentIDs(childrenOf: proposedDestination.equipmentID).first,
               let coinState = snapshot.state(matching: childId) as? CoinState {
                if !coinState.collected {
                    interaction.addAction(CollectCoin(playerId: interaction.value.controlledEquipmentID, coinId: childId))
                }
            }
        }
        game.programmaticPlayerInteractions.removeValue(forKey: interaction.value.id)
        return
    }
    //...
```

Finally, if the landing site isn’t a valid location, `endJump` returns the player to their starting position and decrements their health.

```swift
    // If the player doesn't land on a valid destination, return them to their starting position.
    let player = game.tabletopGame.equipment(of: Player.self, matching: interaction.value.controlledEquipmentID)!
    interaction.addAction(.moveEquipment(matching: player.id, childOf: .bankID(for: player.seat), pose: .identity))
    interaction.addAction(DecrementHealth(playerId: interaction.value.controlledEquipmentID))
    game.programmaticPlayerInteractions.removeValue(forKey: interaction.value.id)
}
```

The `GameObserver` class is responsible for reacting to confirmed game actions. The game decrements a player’s health when the player lands in the water, or if they fail to jump again quickly after landing on a lily pad before it sinks. Within `actionWasConfirmed()`, the game resets the player’s state if the newly provided [`TableSnapshot`](tablesnapshot.md) matches a `ResetPlayer` action. The actions can have other possible matches, like `DecrementHealth` where the game decrements the player’s health, or `CollectCoin` where the player collects a coin at the player’s new location. The game ends when the players collect all of the coins, or when all of the players run out of lives.

```swift
class GameObserver: TabletopGame.Observer {
    func actionWasConfirmed(_ action: some TabletopAction, oldSnapshot: TableSnapshot, newSnapshot: TableSnapshot) {
        
        guard let game else {
            return
        }
        
        if let resetPlayerAction = ResetPlayer(from: action) {
            let (equip, state) = newSnapshot.equipment(of: Player.self, matching: [resetPlayerAction.playerId]).first!
            game.playerStats[equip.seat].health = state.health
            game.playerStats[equip.seat].coinsCount = state.coinsCount
            
            return
        }
        
        if let decrementHealthAction = DecrementHealth(from: action) {
            let (equip, state) = newSnapshot.equipment(of: Player.self, matching: [decrementHealthAction.playerId]).first!
            game.playerStats[equip.seat].health = state.health
            
            // Freeze the player when their health equals `0`.
            if action.playerID == game.tabletopGame.localPlayer.id && state.health == 0 {
                game.tabletopGame.addAction(FreezePlayer(playerId: equip.id))
            }
            
            return
        }
        
        if let collectCoinAction = CollectCoin(from: action) {
            let (equip, playerState) = newSnapshot.equipment(of: Player.self, matching: [collectCoinAction.playerId]).first!
            game.playerStats[equip.seat].coinsCount = playerState.coinsCount
            
            return
        }
    }
}
```

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [class TabletopGame](tabletopgame.md)
  An object that manages the setup and gameplay of a tabletop game.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/synchronizing-group-gameplay-with-tabletopkit)*