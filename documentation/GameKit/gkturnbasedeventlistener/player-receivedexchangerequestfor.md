# player(_:receivedExchangeRequest:for:)

**Framework**: GameKit  
**Kind**: method

Handles when the local player receives an exchange request from another participant.

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
optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

Reply to this exchange request using the `GKTurnBasedExchange` [`reply(withLocalizableMessageKey:arguments:data:completionHandler:)`](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `exchange`: The exchange request sent from the other participant.
- `match`: The match related to this turn-based event.

## See Also

- [func player(GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md)
  Handles when all recipients of an exchange request respond.
- [func player(GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md)
  Handles when the sender cancels an exchange request they intiated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangerequest:for:))*