# GKMatch

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

A peer-to-peer network between a group of players that sign into Game Center.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKMatch
```

```objc
@interface GKMatch : NSObject
```

## Mentions

- [Finding multiple players for a game](./finding-multiple-players-for-a-game.md)
- [Assigning players to teams using rules](./assigning-players-to-teams-using-rules.md)
- [Creating activities for your game](./creating-activities-for-your-game.md)

#### Overview

Matches provide a mechanism for a player to send both game and voice data to other players.

You never create a `GKMatch` object directly. Instead, GameKit passes a match object to a [`GKMatchmakerViewControllerDelegate`](./gkmatchmakerviewcontrollerdelegate.md) method or a [`GKMatchmaker`](./gkmatchmaker.md) handler when you set up a multiplayer game. For details, see [Finding multiple players for a game](./finding-multiple-players-for-a-game.md).

If you use the [`GKMatchmakerViewController`](./gkmatchmakerviewcontroller.md) class to find players, implement the [`matchmakerViewController(_:didFind:)`](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didfind%29.md) delegate method to set the match delegate. If you use the [`GKMatchmaker`](./gkmatchmaker.md) class, set the match delegate in the handler you pass to the [`findMatch(for:withCompletionHandler:)`](./gkmatchmaker/findmatch%28for,withcompletionhandler%29.md) method.

You can begin exchanging data when two or more players join the match. Implement the [`match(_:player:didChange:)`](./gkmatchdelegate/match%28_,player,didchange%29-8ohgr.md) delegate method to track when players connect or disconnect from the match. Then use either the [`sendData(toAllPlayers:with:)`](./gkmatch/senddata%28toallplayers,with%29.md) or the [`send(_:to:dataMode:)`](./gkmatch/send%28_,to,datamode%29.md) method to send data. To process the data on the recipient side, implement the [`match(_:didReceive:fromRemotePlayer:)`](./gkmatchdelegate/match%28_,didreceive,fromremoteplayer%29.md) delegate method.

To implement voice chat, use the [`voiceChat(withName:)`](./gkmatch/voicechat%28withname%29.md) method to create one or more voice channels represented by the returned [`GKVoiceChat`](./gkvoicechat.md) object.

When you’re finished with a match, call the [`disconnect()`](./gkmatch/disconnect%28%29.md) method and set the match’s delegate to `nil`. Otherwise, GameKit may send [`match(_:player:didChange:)`](./gkmatchdelegate/match%28_,player,didchange%29-8ohgr.md) to the delegate until all players disconnect from the match.

## Topics

### Setting the delegate
- [var delegate: (any GKMatchDelegate)?](./gkmatch/delegate.md)
  The delegate that handles communication between players in a match.
- [protocol GKMatchDelegate](./gkmatchdelegate.md)
  An object that receives connection status and data transmitted in a multiplayer game.
### Working with other players
- [var expectedPlayerCount: Int](./gkmatch/expectedplayercount.md)
  The remaining number of players invited but not yet connected to the match.
- [var players: [GKPlayer]](./gkmatch/players.md)
  The players that join the match.
### Sending data to other players
- [func chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Void)](./gkmatch/choosebesthostingplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server topology.
- [func send(Data, to: [GKPlayer], dataMode: GKMatch.SendDataMode) throws](./gkmatch/send%28_,to,datamode%29.md)
  Transmits data to one or more players connected to the match.
- [func sendData(toAllPlayers: Data, with: GKMatch.SendDataMode) throws](./gkmatch/senddata%28toallplayers,with%29.md)
  Transmits data to all players connected to the match.
- [GKMatch.SendDataMode](./gkmatch/senddatamode.md)
  The mechanism used to transmit data to other players.
### Joining a voice chat
- [func voiceChat(withName: String) -> GKVoiceChat?](./gkmatch/voicechat%28withname%29.md)
  Joins the local player to a voice channel.
### Getting matchmaking properties
- [var properties: [String : Any]?](./gkmatch/properties.md)
  The local player’s properties that matchmaking rules used to find the players with some additions.
- [var playerProperties: [GKPlayer : [String : Any]]?](./gkmatch/playerproperties.md)
  The properties for other players that matchmaking rules uses to find players, with some additions.
### Finishing the match
- [func disconnect()](./gkmatch/disconnect%28%29.md)
  Disconnects the local player from the match.
- [func rematch(completionHandler: ((GKMatch?, (any Error)?) -> Void)?)](./gkmatch/rematch%28completionhandler%29.md)
  Creates a new match with the players from an existing match.
### Deprecated Methods and Properties
- [func chooseBestHostPlayer(completionHandler: (String?) -> Void)](./gkmatch/choosebesthostplayer%28completionhandler%29.md)
  Determines the best player in the game to act as the server for a client-server match.
- [var playerIDs: [String]?](./gkmatch/playerids.md)
  The player identifiers for remote players in the match.
- [func send(Data, toPlayers: [String], with: GKMatch.SendDataMode) throws](./gkmatch/send%28_,toplayers,with%29.md)
  Transmits data to a list of connected players.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Real-time games
- [Creating real-time games](./creating-real-time-games.md)
  Develop games where multiple players interact in real time.
- [Finding multiple players for a game](./finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](./exchanging-data-between-players-in-real-time-games.md)
  Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](./adding-voice-chat-to-multiplayer-games.md)
  Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [Finding players for custom server-based games](./finding-players-for-custom-server-based-games.md)
  Connect players to your custom server-hosted games by creating game sessions with hosted matches.
- [Matchmaking rules](./matchmaking-rules.md)
  Game Center applies different type of rules you create in a particular order to find the best matches.
- [class GKMatchRequest](./gkmatchrequest.md)
  An object that encapsulates the parameters to create a real-time or turn-based match.
- [class GKMatchmaker](./gkmatchmaker.md)
  An object that creates matches with other players without presenting an interface to the players.
- [class GKMatchmakerViewController](./gkmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.
- [protocol GKInviteEventListener](./gkinviteeventlistener.md)
  A protocol that handles invite events from Game Center.
- [class GKInvite](./gkinvite.md)
  An invitation to join a match sent to the local player from another player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch)*