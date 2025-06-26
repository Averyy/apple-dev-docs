# GKTurnBasedEventListener

**Framework**: GameKit  
**Kind**: protocol

The protocol that handles turn-based and data-exchange events between participants in a match.

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
protocol GKTurnBasedEventListener
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Overview

To receive the `GKTurnBasedEventListener` call backs, register your game object with the local player object immediately after initialization.

```swift
GKLocalPlayer.local.register(self)
```

Adopt the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol to handle a variety of Game Center events instead of the individual [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocols.

Then implement the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) and other `GKTurnBasedEventListener` protocol methods to handle turn-based events that occur throughout a match.

## Topics

### Handling Match-Related Events
- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:).md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:matchended:).md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:wantstoquitmatch:).md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles when the player uses Game Center to start a match with other players.
### Handling Data Exchanges
- [func player(GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md)
  Handles when the local player receives an exchange request from another participant.
- [func player(GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md)
  Handles when all recipients of an exchange request respond.
- [func player(GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md)
  Handles when the sender cancels an exchange request they intiated.

## Relationships

### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)

## See Also

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
  Let Game Center store and forward match data between players in a turn-based game.
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)
  Notify players of match events by sending messages and game data.
- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)
  Add the ability for players to exchange game data and send messages while waiting for their turns.
- [class GKTurnBasedMatchmakerViewController](gkturnbasedmatchmakerviewcontroller.md)
  An interface that allows a player to invite other players to a turn-based match and automatch to fill any empty slots.
- [class GKTurnBasedMatch](gkturnbasedmatch.md)
  An object that encapsulates the match data for games where players take turns.
- [class GKTurnBasedParticipant](gkturnbasedparticipant.md)
  A participant in a turn-based match.
- [class GKTurnBasedExchange](gkturnbasedexchange.md)
  Exchange request information that participants send in a turn-based match.
- [class GKTurnBasedExchangeReply](gkturnbasedexchangereply.md)
  Details about a recipient’s response to an exchange request.
- [GKGameCenterBadgingDisabled](../BundleResources/Information-Property-List/GKGameCenterBadgingDisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener)*