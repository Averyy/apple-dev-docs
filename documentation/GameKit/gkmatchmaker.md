# GKMatchmaker

**Framework**: GameKit  
**Kind**: class

An object that creates matches with other players without presenting an interface to the players.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKMatchmaker
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)

#### Overview

Use the `GKMatchmaker` class to auto-match players for a quicker game start, programmatically invite specific players, or implement your own interface for players to invite other players. If you want to present a familiar matchmaking GameKit interface to players, instead use either the [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) or [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) class.

If you host a game on your own server, you can also use this class to find Game Center players. That is, you implement the networking and communication between the players through your own servers not Game Center.

To find players using this class, create a [`GKMatchRequest`](gkmatchrequest.md) object and configure it according to the parameters of your game. Then, pass the match request and a handler using the [`findMatch(for:withCompletionHandler:)`](gkmatchmaker/findmatch(for:withcompletionhandler:).md) method, or the [`findPlayers(forHostedMatchRequest:withCompletionHandler:)`](gkmatchmaker/findplayers(forhostedmatchrequest:withcompletionhandler:).md) method for hosted games, to the shared `GKMatchmaker` object.

GameKit calls the handler when players accept their invitations. Implement the handler to set the delegate of the [`GKMatch`](gkmatch.md) object that GameKit sends and start the game when there are enough players.

If the match doesn’t have enough players (for example, some players decline their invitations), you can create another match request and call the [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) method repeatedly until the match’s [`expectedPlayerCount`](gkmatch/expectedplayercount.md) property is zero. When you have enough players to start the match, call the [`finishMatchmaking(for:)`](gkmatchmaker/finishmatchmaking(for:).md) method to end the matchmaking process.

If you provide a SharePlay interface for inviting players, use the [`startGroupActivity(playerHandler:)`](gkmatchmaker/startgroupactivity(playerhandler:).md) and [`stopGroupActivity()`](gkmatchmaker/stopgroupactivity().md) methods to create a group activity on behalf of the player.

## Topics

### Retrieving the shared matchmaker
- [class func shared() -> GKMatchmaker](gkmatchmaker/shared.md)
  Returns the singleton matchmaker instance.
### Receiving invitations from other players
- [func match(for: GKInvite, completionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/match(for:completionhandler:).md)
  Creates a match from an invitation that the local player accepts.
### Matching players
- [func findMatch(for: GKMatchRequest, withCompletionHandler: ((GKMatch?, (any Error)?) -> Void)?)](gkmatchmaker/findmatch(for:withcompletionhandler:).md)
  Initiates a request to find players for a peer-to-peer match.
- [func findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, (any Error)?) -> Void)?)](gkmatchmaker/findplayers(forhostedrequest:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match.
- [func findMatchedPlayers(GKMatchRequest, withCompletionHandler: (GKMatchedPlayers?, (any Error)?) -> Void)](gkmatchmaker/findmatchedplayers(_:withcompletionhandler:).md)
  Initiates a request to find players for a hosted match that uses matchmaking rules.
- [class GKMatchedPlayers](gkmatchedplayers.md)
  An object that represents matchmaking results, including the players that join the match and their properties that matchmaking rules uses.
- [func addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: (((any Error)?) -> Void)?)](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md)
  Invites additional players to an existing match.
- [func finishMatchmaking(for: GKMatch)](gkmatchmaker/finishmatchmaking(for:).md)
  Informs the server when programmatic matchmaking finishes.
- [func cancel()](gkmatchmaker/cancel.md)
  Cancels a matchmaking request.
- [func cancelPendingInvite(to: GKPlayer)](gkmatchmaker/cancelpendinginvite(to:).md)
  Cancels a pending invitation to another player.
### Finding players who request matches
- [func queryActivity(completionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryactivity(completionhandler:).md)
  Finds the number of players, across player groups, who recently requested a match.
- [func queryPlayerGroupActivity(Int, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryplayergroupactivity(_:withcompletionhandler:).md)
  Finds the number of players in a player group who recently requested a match.
- [func queryQueueActivity(String, withCompletionHandler: ((Int, (any Error)?) -> Void)?)](gkmatchmaker/queryqueueactivity(_:withcompletionhandler:).md)
  Finds the number of players in a specific queue who recently requested a match.
### Looking for nearby players
- [func startBrowsingForNearbyPlayers(handler: ((GKPlayer, Bool) -> Void)?)](gkmatchmaker/startbrowsingfornearbyplayers(handler:).md)
  Finds nearby players through Bluetooth or WiFi on the same subnet.
- [func stopBrowsingForNearbyPlayers()](gkmatchmaker/stopbrowsingfornearbyplayers.md)
  Stops finding nearby players.
### Starting matches using SharePlay
- [func startGroupActivity(playerHandler: (GKPlayer) -> Void)](gkmatchmaker/startgroupactivity(playerhandler:).md)
  Begins a SharePlay activity for your game when a FaceTime call is active.
- [func stopGroupActivity()](gkmatchmaker/stopgroupactivity.md)
  Ends a SharePlay activity for the entire group, which the local player activates.
### Deprecated
- [Deprecated Symbols](gkmatchmaker-deprecated-symbols.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating real-time games](creating-real-time-games.md)
  Develop games where multiple players interact in real time.
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
  Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)
  Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [Finding players for custom server-based games](finding-players-for-custom-server-based-games.md)
  Connect players to your custom server-hosted games by creating game sessions with hosted matches.
- [Matchmaking rules](matchmaking-rules.md)
  Game Center applies different type of rules you create in a particular order to find the best matches.
- [class GKMatchRequest](gkmatchrequest.md)
  An object that encapsulates the parameters to create a real-time or turn-based match.
- [class GKMatchmakerViewController](gkmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.
- [protocol GKInviteEventListener](gkinviteeventlistener.md)
  A protocol that handles invite events from Game Center.
- [class GKInvite](gkinvite.md)
  An invitation to join a match sent to the local player from another player.
- [class GKMatch](gkmatch.md)
  A peer-to-peer network between a group of players that sign into Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker)*