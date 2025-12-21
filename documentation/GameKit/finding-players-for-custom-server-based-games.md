# Finding players for custom server-based games

**Framework**: GameKit

Connect players to your custom server-hosted games by creating game sessions with hosted matches.

#### Overview

Hosted matches allow your game to use the Game Center matchmaking service to find players while using your own server to exchange game data. This approach gives you more control over the networking architecture. You can quickly find players for your game with hosted matches by using the Game Center service and optionally use matchmaking rules to filter and prioritize match requests to find the most compatible players.

When you implement hosted matches, Game Center handles the matchmaking process but returns player identifiers instead of a complete match object. Your game then connects each player to your server, which becomes responsible for routing network data between players.

Creating a hosted match requires your game to implement all of the low-level networking needed for your game. In particular, design and implement:

- Networking code to connect each device to your server
- A networking protocol to inform other devices of the state of any participant in the match
- A service to map player identifiers to the specific device connected to your server

If your game uses the standard matchmaking user interface in GameKit, each device needs to inform GameKit after it connects to your server. This information allows GameKit to update its user interface.

##### Use the Game Center Interface or Programmatic Matchmaking

You can present a Game Center interface for the local player to discover and invite other players to participate. Alternatively, you can present your own custom interface to connect players or match players without presenting an interface.

In your code, you create a match request and optionally present the matchmaker view controller. Then you implement methods to handle the process of receiving and accepting invitations. The code you write for hosted matchmaking is similar to the code you write for real-time matches.

> **Note**: Features in real-time matchmaking compose key parts of game creation with hosted matches. For more information, see [`Start a real-time match`](creating-real-time-games#Start-a-real-time-match.md).

The critical difference between the two models is that hosted matchmaking returns player identifiers instead of a completed match object. Your game then connects that player to your own server. Your server must match that player’s network address to the player identifier and, similar to a match, perform routing when one device in the match needs to communicate with others.

The following table lists the most common methods for real-time matchmaking and the corresponding methods or implementation details for hosted matchmaking.

| Real-time matchmaking | Hosted matchmaking |
| --- | --- |
| Your view controller delegate implements the [`matchmakerViewController(_:didFind:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md) method to receive the match. | Your delegate implements the [`matchmakerViewController(_:hostedPlayerDidAccept:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:hostedplayerdidaccept:).md) method to receive a notification that a player has accepted an invitation to join the match. |
| Your programmatic matchmaking code calls [`findMatch(for:withCompletionHandler:)`](gkmatchmaker/findmatch(for:withcompletionhandler:).md) to create a new match. | Your programmatic code calls [`findPlayers(forHostedRequest:withCompletionHandler:)`](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md) to find a set of new players for a match. Alternatively, call [`findMatchedPlayers(_:withCompletionHandler:)`](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md) to find players using matchmaking rules. |
| Your programmatic code calls [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) to add players to a match. | Your programmatic code calls `findPlayers(forHostedRequest:withCompletionHandler:)` or `findMatchedPlayers(_:withCompletionHandler:)` to find a set of new players for a match. Because you implement your own matching architecture, you decide when to make this call and whether you’re adding players to an existing hosted match. |
| Your game receives an invitation. | The [`GKInvite`](gkinvite.md) object’s [`isHosted`](gkinvite/ishosted.md) property tells you whether the match is a hosted match. This matters only if your game implements both hosted and nonhosted matches. |

##### Create a Hosted Match with the Game Center Interface

Your players can send invites to fill empty player slots and start a game by using the default matchmaking interface. To create a hosted match using [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md):

1. Create and configure a new [`GKMatchRequest`](gkmatchrequest.md).
2. Initialize a new `GKMatchmakerViewController` instance using the match request.
3. Set the `GKMatchmakerViewController` instance’s [`isHosted`](gkmatchmakerviewcontroller/ishosted.md) property to `true`.
4. Make your presenting view controller the matchmaking view controller’s delegate.
5. Present the matchmaking interface.

The player interacts with the matchmaking screen until the match is ready to start or an error occurs. Handle matchmaking changes and errors from `GKMatchmakerViewController` by setting the [`matchmakerDelegate`](gkmatchmakerviewcontroller/matchmakerdelegate.md) with an object that notifies you when players accept their invitations. As a hosted view controller, your `matchmakerDelegate` implements [`matchmakerViewController(_:hostedPlayerDidAccept:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:hostedplayerdidaccept:).md) to process new players, and [`matchmakerViewController(_:didFailWithError:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfailwitherror:).md) to handle errors. Your delegate needs to behave differently depending on which device your game is running on:

- When called on the new player’s device, the device needs to connect to your own server. When successfully connected, call the [`setHostedPlayer(_:didConnect:)`](gkmatchmakerviewcontroller/sethostedplayer(_:didconnect:).md) method to tell the view controller that the player has connected to the match.
- When called on another player’s device, the players’s game needs to determine that it can talk to the new player’s device through your server connection. When the game knows it can send messages to the new player, call the `setHostedPlayer(_:didConnect:)` method to update the user interface.

The following code example implements `matchmakerDelegate` methods to connect new players to a server and inform Game Center of the connections:

```swift
@MainActor func matchmakerViewController(_ viewController: GKMatchmakerViewController,
                             hostedPlayerDidAccept player: GKPlayer) {
    // Connect the player to your game server.
    connectPlayerToServer(with: player, completion: { success in
        if success {
            // Inform GameKit that the player is connected.
            viewController.setHostedPlayer(player, didConnect: true)
        }
    })
}

// Implement your custom networking code to connect to your server.
// Map the `gamePlayerID` from the `GKPlayer` to your server connection.
func connectPlayerToServer(with player: GKPlayer, completion: (Bool) -> Void) {
    // Get the player identifier.
    let playerIdentifier = player.gamePlayerID
    print("Connect player with ID: \(playerIdentifier).")
}

func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController) {
    dismiss(animated: true)
}

// Handle a matchmaking error.
func matchmakerViewController(_ viewController: GKMatchmakerViewController,
                             didFailWithError error: Error) {
    print("Matchmaking failed: \(error.localizedDescription)")
    dismiss(animated: true)
}

func dismiss(animated: Bool) {
    print("Dismiss the matchmaking view.")
}
```

When all of the players accept their invitations to a match, GameKit invokes [`matchmakerViewController(_:didFindHostedPlayers:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindhostedplayers:).md) in the app instances for all players in the game, including the local player who initiates the invitations. Start the game by dismissing the view controller and connecting the players through your own server.

#### Dismiss the Matchmaker View Controller

After all invitees have accepted your app’s match request, you send the information about the players to your server. Then, send a start-game message to all of the invitees. When invitees receive the start-game message, they must manually close the view controller for their app.

```swift
func startGameWithAllPlayers(players: [GKPlayer], viewController: GKMatchmakerViewController) {
    // Send information about all players to your game server.
    connectAllPlayersToServer(players: players) { success in
        if success {
            // Send a start game message to all connected players, dismiss
            // the matchmaker view controller and transition to your game's
            // main interface.
        } else {
            // Alert the player that connection failed.
        }
    }
}

func connectAllPlayersToServer(players: [GKPlayer], completion: @escaping (Bool) -> Void) {
        print("Connect all players to server.")
}
```

#### Start a Hosted Match Programmatically

Without the default Game Center interface, your app can start hosted matches by programmatically inviting players. The following example starts a match by calling [`findPlayers(forHostedRequest:withCompletionHandler:)`](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md) and connecting players in the completion handler:

```swift
func findHostedMatch() async throws {
    // Create and configure a match request.
    let request = GKMatchRequest()
    request.minPlayers = 2
    request.maxPlayers = 8
    
    // Find players
    GKMatchmaker.shared().findPlayers(forHostedRequest: request, withCompletionHandler: { (players: [GKPlayer]?, error: Error?) -> Void in
        print("Found players: \(String(describing: players))")
        
        if let error = error {
            // Handle the error.
            print("Error finding players: \(error.localizedDescription)")
            return
        }
        
        // Exit if no players were found.
        guard let players = players else { return }
        
        // Connect to your game server with the player information.
        connectPlayersToHostedMatch(players: players)
    })
}

// Implement your custom networking code to connect to your server.
func connectPlayersToHostedMatch(players: [GKPlayer]) {
    // Map the `gamePlayerID` for each `GKPlayer` to your server connections.
}
```

#### Start a Hosted Match with Matchmaking Rules

You can find players for a hosted match with matchmaking rules by initiating a request with [`findMatchedPlayers(_:withCompletionHandler:)`](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md). Set the rules-related properties in the [`GKMatchRequest`](gkmatchrequest.md) ([`queueName`](gkmatchrequest/queuename.md) and optionally, [`properties`](gkmatchrequest/properties.md)) before you call this method. In this example, the app connects players using a match request configured with matchmaking rules:

```swift
func findHostedMatchWithRules() async throws {
    // Create and configure a match request.
    let request = GKMatchRequest()
    request.minPlayers = 2
    request.maxPlayers = 8
    
    // Set up matchmaking rules.
    
    // 1. Set the queue name - this identifies which rule set to use.
    // Assign the name of a queue you've configured in App Store Connect.
    request.queueName = "competitive-queue"
    
    // 2. Set additional properties for matchmaking (optional).
    // These are key-value pairs your game uses for additional matching
    // criteria. The specific keys and values should align with the rules
    // you've defined in App Store Connect.
    request.properties = [
        "region": "us-west",
        "difficulty": "expert",
        "gameVersion": "1.2.3"
    ]
    
    // Find players using rule-based matchmaking.
    GKMatchmaker.shared().findMatchedPlayers(request, withCompletionHandler: { (players: GKMatchedPlayers?, error: Error?) -> Void in
        if let error = error {
            print("Error finding players: \(error.localizedDescription)")
            return
        }
        
        guard let matchedPlayers = players, !matchedPlayers.players.isEmpty else {
            print("No players found matching the criteria")
            return
        }
        
        print("Found \(matchedPlayers.players.count) players matching the rules criteria")
        
        // Connect matched players to your game server.
        connectPlayersToHostedMatch(players: matchedPlayers.players)
    })
}

// Implement your custom networking code to connect to your server.
func connectPlayersToHostedMatch(players: [GKPlayer]) {    
    // Map the `gamePlayerID` for each `GKPlayer` to your server connections.
}
```

For more information on creating rules-based matches, see [`Create match requests that use the matchmaking rules`](finding-players-using-matchmaking-rules#Create-match-requests-that-use-the-matchmaking-rules.md).

## See Also

- [Creating real-time games](creating-real-time-games.md)
  Develop games where multiple players interact in real time.
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
  Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)
  Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [Matchmaking rules](matchmaking-rules.md)
  Game Center applies different type of rules you create in a particular order to find the best matches.
- [class GKMatchRequest](gkmatchrequest.md)
  An object that encapsulates the parameters to create a real-time or turn-based match.
- [class GKMatchmaker](gkmatchmaker.md)
  An object that creates matches with other players without presenting an interface to the players.
- [class GKMatchmakerViewController](gkmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.
- [protocol GKInviteEventListener](gkinviteeventlistener.md)
  A protocol that handles invite events from Game Center.
- [class GKInvite](gkinvite.md)
  An invitation to join a match sent to the local player from another player.
- [class GKMatch](gkmatch.md)
  A peer-to-peer network between a group of players that sign into Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/finding-players-for-custom-server-based-games)*