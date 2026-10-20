# player(_:receivedExchangeCancellation:for:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when the sender cancels an exchange request they intiated.

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
optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)
```

```objc
- (void) player:(GKPlayer *) player receivedExchangeCancellation:(GKTurnBasedExchange *) exchange forMatch:(GKTurnBasedMatch *) match;
```

## Mentions

- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## Parameters

- `player`: The player who receives this turn-based event.
- `exchange`: The exchange request that the sender cancels.
- `match`: The match related to this turn-based event.

## See Also

### Handling Data Exchanges
- [func player(GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangerequest,for%29.md)
  Handles when the local player receives an exchange request from another participant.
- [func player(GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangereplies,forcompletedexchange,for%29.md)
  Handles when all recipients of an exchange request respond.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:))*