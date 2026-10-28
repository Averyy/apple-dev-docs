# player(_:receivedExchangeRequest:for:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) player:(GKPlayer *) player receivedExchangeRequest:(GKTurnBasedExchange *) exchange forMatch:(GKTurnBasedMatch *) match;
```

## Mentions

- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## Discussion

Reply to this exchange request using the `GKTurnBasedExchange` [`reply(withLocalizableMessageKey:arguments:data:completionHandler:)`](../gkturnbasedexchange/reply%28withlocalizablemessagekey,arguments,data,completionhandler%29.md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `exchange`: The exchange request sent from the other participant.
- `match`: The match related to this turn-based event.

## See Also

### Handling Data Exchanges
- [func player(GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangereplies,forcompletedexchange,for%29.md)
  Handles when all recipients of an exchange request respond.
- [func player(GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangecancellation,for%29.md)
  Handles when the sender cancels an exchange request they intiated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangerequest:for:))*