# GKTurnBasedExchange

**Framework**: GameKit  
**Kind**: class

Exchange request information that participants send in a turn-based match.

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
class GKTurnBasedExchange
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)

#### Overview

GameKit sends exchange objects to [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) protocol methods when the local player receives an exchange request or recipients reply to an exchange request. The exchange object encapsulates your custom game data that you want to communicate to other players.

You initiate an exchange request using the `GKTurnBasedMatch` [`sendExchange(to:data:localizableMessageKey:arguments:timeout:completionHandler:)`](gkturnbasedmatch/sendexchange(to:data:localizablemessagekey:arguments:timeout:completionhandler:).md) method. Then GameKit sends the request to the recipients passing the exchange object to the `GKTurnBasedEventListener` [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) protocol method. GameKit sets the status of the exchange object to [`GKTurnBasedExchangeStatus.active`](gkturnbasedexchangestatus/active.md).

After all recipients respond to the request, using the [`reply(withLocalizableMessageKey:arguments:data:completionHandler:)`](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md) method, or exceed the time out specified in the request, GameKit sends the exchange to the sender and the current participant. GameKit sets the exchange status to [`GKTurnBasedExchangeStatus.complete`](gkturnbasedexchangestatus/complete.md) and then passes it to the `GKTurnBasedEventListener` [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) method.

Before the current participant ends their turn, save the completed exchanges using the `GKTurnBasedMatch` [`saveMergedMatch(_:withResolvedExchanges:completionHandler:)`](gkturnbasedmatch/savemergedmatch(_:withresolvedexchanges:completionhandler:).md) method. Get the exchanges from the match object using the [`completedExchanges`](gkturnbasedmatch/completedexchanges.md) property. Alternatively, save exchange data in the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) protocol method when all recipients reply to specific exchange requests.

To cancel an active or complete exchange, use the [`cancel(withLocalizableMessageKey:arguments:completionHandler:)`](gkturnbasedexchange/cancel(withlocalizablemessagekey:arguments:completionhandler:).md) method. GameKit notifies the recipients when the player cancels an exchange, using the `GKTurnBasedEventListener` [`player(_:receivedExchangeCancellation:for:)`](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md) protocol method.

## Topics

### Retrieving Exchange Details
- [var exchangeID: String](gkturnbasedexchange/exchangeid.md)
  The identifier for the exchange request.
- [var sender: GKTurnBasedParticipant](gkturnbasedexchange/sender.md)
  The participant who sends the exchange request to recipients.
- [var recipients: [GKTurnBasedParticipant]](gkturnbasedexchange/recipients.md)
  The participants who receives the exchange request.
- [var data: Data?](gkturnbasedexchange/data.md)
  The game-specific exchange data that GameKit sends to participants.
- [var message: String?](gkturnbasedexchange/message.md)
  A localized message from the sender to the recipients of an exchange request.
- [var sendDate: Date](gkturnbasedexchange/senddate.md)
  The date that the sender initiates the exchange request.
- [var timeoutDate: Date?](gkturnbasedexchange/timeoutdate.md)
  The date that the recipients must reply by before the exchange request times out.
### Replying to Exchange Requests
- [func reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md)
  Replies to an exchange request on behalf of a recipient.
- [var replies: [GKTurnBasedExchangeReply]?](gkturnbasedexchange/replies.md)
  The replies from recipients of the exchange request.
- [var status: GKTurnBasedExchangeStatus](gkturnbasedexchange/status.md)
  The status of the exchange request.
- [enum GKTurnBasedExchangeStatus](gkturnbasedexchangestatus.md)
  The status of an exchange or reply.
- [var completionDate: Date?](gkturnbasedexchange/completiondate.md)
  The date when all recipients of the exchange request reply.
### Canceling Exchange Requests
- [func cancel(withLocalizableMessageKey: String, arguments: [String], completionHandler: (((any Error)?) -> Void)?)](gkturnbasedexchange/cancel(withlocalizablemessagekey:arguments:completionhandler:).md)
  Cancels an exchange request.

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
- [class GKTurnBasedExchangeReply](gkturnbasedexchangereply.md)
  Details about a recipient’s response to an exchange request.
- [GKGameCenterBadgingDisabled](../BundleResources/Information-Property-List/GKGameCenterBadgingDisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)*