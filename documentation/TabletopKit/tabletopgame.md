# TabletopGame

**Framework**: TabletopKit  
**Kind**: class

An object that manages the setup and gameplay of a tabletop game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
class TabletopGame
```

#### Overview

First, create a [`TableSetup`](tablesetup.md) object that represents your game layout and equipment. Add seats for players to occupy, conforming to the [`TableSeat`](tableseat.md) protocol, and equipment for them to manipulate, conforming to the [`Equipment`](equipment.md) protocol.

Pass an object that conforms to the [`Tabletop`](tabletop.md) or [`EntityTabletop`](entitytabletop.md) protocol to the [`TableSetup`](tablesetup.md) initializer.

```swift
let table = Table()
root = createRootEntity(table: table.entity)
var setup = TableSetup(tabletop: table)
```

Implement your structure to initialize the protocol properties, such as `shape`, `entity`, and `id` properties for the `EntityTabletop` protocol.

```swift
struct Table: EntityTabletop {
    var shape: TabletopShape
    var entity: Entity
    var id: EquipmentIdentifier
    
    init() {
        self.entity = try! Entity.load(named: "table/table", in: contentBundle)
        self.shape = .round(entity: entity)
        self.id = .table
    }
}
```

Then, create the `TabletopGame` object that represents your game instance by passing the `TableSetup` object to the [`init(tableSetup:version:)`](tabletopgame/init(tablesetup:version:).md) initializer.

```swift
game = TabletopGame(tableSetup: setup)
```

Place the [`localPlayer`](tabletopgame/localplayer.md) in a seat at the table using [`claimSeat(_:)`](tabletopgame/claimseat(_:).md) or a similar method.

```swift
game.claimAnySeat()
```

Next, implement an object that renders your game layout and equipment. Set the game’s renderer, conforming to the [`TabletopGame.RenderDelegate`](tabletopgame/renderdelegate.md) protocol, using the [`addRenderDelegate(_:)`](tabletopgame/addrenderdelegate(_:).md) method. Implement the [`onUpdate(timeInterval:snapshot:visualState:)`](tabletopgame/renderdelegate/onupdate(timeinterval:snapshot:visualstate:).md) method to render the current state of the game. Alternatively, conform to the [`EntityRenderDelegate`](entityrenderdelegate.md) protocol.

```swift
game.addRenderDelegate(self)
```

If needed, you can draw a debug representation of selected items in the game using the [`debugDraw(options:)`](tabletopgame/debugdraw(options:).md) method.

```swift
game.debugDraw(options: [.drawTable, .drawSeats, .drawEquipment])
```

Then, add actions to the equipment that controls gameplay using the `addAction(_:)` and [`addActions(_:)`](tabletopgame/addactions(_:).md) methods.

Finally, pass an object to the [`addObserver(_:)`](tabletopgame/addobserver(_:).md) method that conforms to the [`TabletopGame.Observer`](tabletopgame/observer.md) protocol. Implement the `Observer` protocol methods to progress gameplay when players interact with the equipment.

## Topics

### Creating a tabletop game
- [init(tableSetup: TableSetup, version: Int)](tabletopgame/init(tablesetup:version:).md)
  Creates a tabletop game with the specified table configuration and version of rules.
- [var rootPose: Pose3D](tabletopgame/rootpose.md)
  Update the root pose for the current player
- [func update(deltaTime: Double)](tabletopgame/update(deltatime:).md)
  Update the game manually. Call this function if `automaticUpdate` was not set when registering the Tabletop instance.
- [func withCurrentSnapshot((TableSnapshot) -> Void)](tabletopgame/withcurrentsnapshot(_:).md)
### Adding equipment to the game
- [var equipment: [any Equipment]](tabletopgame/equipment.md)
- [var equipmentIDs: [EquipmentIdentifier]](tabletopgame/equipmentids.md)
- [func equipment(matching: EquipmentIdentifier) -> (any Equipment)?](tabletopgame/equipment(matching:).md)
- [func equipment<E>(of: E.Type) -> [E]](tabletopgame/equipment(of:).md)
- [func equipment<E>(of: E.Type, forEntity: Entity) -> E?](tabletopgame/equipment(of:forentity:).md)
  Retrieves the specified equipment type associated with an entity if it exists.
- [func equipment<E>(of: E.Type, matching: EquipmentIdentifier) -> E?](tabletopgame/equipment(of:matching:).md)
### Managing seats
- [func claimAnySeat()](tabletopgame/claimanyseat.md)
  Claims any free seat. Has no effect if the player is already seated or if there are no free seats.
- [func claimSeat(some TableSeat)](tabletopgame/claimseat(_:).md)
  Claims the given seat. If provided Seat is not part of the table, it has no effect
- [func claimSeat(matching: TableSeatIdentifier)](tabletopgame/claimseat(matching:).md)
  Claims the given seat. If provided ID does not exist, it has no effect
- [func releaseSeat()](tabletopgame/releaseseat.md)
  Releases the seat for this player. If the player is not seated it has no effect
### Getting the player
- [var localPlayer: Player](tabletopgame/localplayer.md)
  The player who runs this tabletop game instance on their device.
### Adding actions
- [func addActions(some Sequence<any TabletopAction>)](tabletopgame/addactions(_:).md)
### Observing actions
- [TabletopGame.Observer](tabletopgame/observer.md)
  A protocol for objects that progress gameplay when players take actions.
- [func addObserver(some TabletopGame.Observer)](tabletopgame/addobserver(_:).md)
- [func removeObserver(some TabletopGame.Observer)](tabletopgame/removeobserver(_:).md)
- [TabletopGame.ActionCancellationReason](tabletopgame/actioncancellationreason.md)
  The possible reasons for cancelling an action or an interaction.
### Jumping to bookmarks
- [func jumpToBookmark(StateBookmark)](tabletopgame/jumptobookmark(_:).md)
  Restores game to the given bookmark
- [func jumpToBookmark(matching: StateBookmarkIdentifier)](tabletopgame/jumptobookmark(matching:).md)
  Restores game to the given bookmark
- [var bookmarks: [StateBookmarkIdentifier]](tabletopgame/bookmarks.md)
### Starting interactions
- [func startInteraction(onEquipmentID: EquipmentIdentifier) -> TabletopInteraction.Identifier?](tabletopgame/startinteraction(onequipmentid:).md)
  Starts a local interaction. It will return `nil` if too many interactions are already happening at the same time.
### Rendering the table
- [func addRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/addrenderdelegate(_:).md)
- [func removeRenderDelegate(some TabletopGame.RenderDelegate)](tabletopgame/removerenderdelegate(_:).md)
- [TabletopGame.RenderDelegate](tabletopgame/renderdelegate.md)
  A protocol for the object that renders your entire game.
- [protocol EntityRenderDelegate](entityrenderdelegate.md)
  A protocol for the object that renders your entire game using RealityKit.
### Supporting multiple players
- [func attachNetworkCoordinator(some TabletopNetworkSessionCoordinator)](tabletopgame/attachnetworkcoordinator(_:).md)
- [func detachNetworkCoordinator()](tabletopgame/detachnetworkcoordinator.md)
- [var multiplayerDelegate: (any TabletopGame.MultiplayerDelegate)?](tabletopgame/multiplayerdelegate-swift.property.md)
- [TabletopGame.MultiplayerDelegate](tabletopgame/multiplayerdelegate-swift.protocol.md)
  An object that handles players joining multiplayer games.
### Enabling group activities
- [func coordinateWithSession(GroupSession<some GroupActivity>)](tabletopgame/coordinatewithsession(_:).md)
  Begins coordination of the game with a group session
### Drawing debug representations
- [func debugDraw(options: DebugDrawOptions)](tabletopgame/debugdraw(options:).md)
  Enable or disable debug visualizations
### Instance Methods
- [func addAction(some TabletopAction)](tabletopgame/addaction(_:)-10j8v.md)
- [func addAction(some CustomAction)](tabletopgame/addaction(_:)-9zgsy.md)
- [func cancelAllInteractions()](tabletopgame/cancelallinteractions.md)
  Cancels all local and remote interactions. This releases control of all the equipment and rolls back all the actions added to the canceled interaction.
- [func cancelInteraction(matching: TabletopInteraction.Identifier)](tabletopgame/cancelinteraction(matching:).md)
  Cancel the local or remote interaction matching the given identifier. This causes any actions added to it to be rolled back, and releases the controlled equipment and any tossed equipment.

## See Also

- [Creating tabletop games](tabletopkitsample.md)
  Develop a spatial board game where multiple players interact with pieces on a table.
- [Synchronizing group gameplay with TabletopKit](synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.
- [struct TableSetup](tablesetup.md)
  An object that represents the arrangement of seats, equipment, and counters around the game table.
- [protocol Tabletop](tabletop.md)
  A protocol for the table surface in your game.
- [protocol EntityTabletop](entitytabletop.md)
  A protocol for the table surface in your game when you render it using RealityKit.
- [struct TabletopShape](tabletopshape.md)
  An object that represents the physical properties of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame)*