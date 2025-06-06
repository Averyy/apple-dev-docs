# GKTurnBasedExchangeReply

**Framework**: GameKit  
**Kind**: class

Details about a recipient’s response to an exchange request.

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
class GKTurnBasedExchangeReply
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Overview

When you accept an exchange request using the [`reply(withLocalizableMessageKey:arguments:data:completionHandler:)`](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md) method, GameKit sends a `GKTurnBasedExchangeReply` object to participants using the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) protocol method. You can also get responses to exchange requests from the [`GKTurnBasedExchange`](gkturnbasedexchange.md) object using the [`replies`](gkturnbasedexchange/replies.md) parameter.

## Topics

### Retrieving Reply Details
- [var data: Data?](gkturnbasedexchangereply/data.md)
  The game-specific data that the recipent provides in the exchange request reply.
- [var message: String?](gkturnbasedexchangereply/message.md)
  A message from the recipient to the sender of the exchange request.
- [var recipient: GKTurnBasedParticipant](gkturnbasedexchangereply/recipient.md)
  The participant who replies to the exchange request.
- [var replyDate: Date](gkturnbasedexchangereply/replydate.md)
  The date the recipient replies to the exchange request.

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
- [protocol GKTurnBasedEventListener](gkturnbasedeventlistener.md)
  The protocol that handles turn-based and data-exchange events between participants in a match.
- [class GKTurnBasedExchange](gkturnbasedexchange.md)
  Exchange request information that participants send in a turn-based match.
- [GKGameCenterBadgingDisabled](../BundleResources/Information-Property-List/GKGameCenterBadgingDisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)*