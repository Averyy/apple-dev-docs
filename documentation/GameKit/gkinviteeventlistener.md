# GKInviteEventListener

**Framework**: GameKit  
**Kind**: protocol

A protocol that handles invite events from Game Center.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKInviteEventListener
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Overview

Implement the methods in the [`GKInviteEventListener`](gkinviteeventlistener.md) protocol to accept invitations from other players or handle when other players accept invitations from the local player.

Adopt the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol to listen for and handle a variety of Game Center events for player accounts instead of the individual [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocols.

For details, see [`Finding multiple players for a game`](finding-multiple-players-for-a-game.md).

## Topics

### Starting a New Match
- [func player(GKPlayer, didAccept: GKInvite)](gkinviteeventlistener/player(_:didaccept:).md)
  Handles the event when the local player accepts an invitation from another player.
- [func player(GKPlayer, didRequestMatchWithRecipients: [GKPlayer])](gkinviteeventlistener/player(_:didrequestmatchwithrecipients:).md)
  Handles the event when the local player sends other players an invitation to join a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkinviteeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles the event when the local player sends other players an invitation to join a match.

## Relationships

### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)

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
- [class GKInvite](gkinvite.md)
  An invitation to join a match sent to the local player from another player.
- [class GKMatch](gkmatch.md)
  A peer-to-peer network between a group of players that sign into Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener)*