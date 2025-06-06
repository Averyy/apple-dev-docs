# player(_:receivedExchangeCancellation:for:)

**Framework**: GameKit  
**Kind**: method

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

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

## Parameters

- `player`: The player who receives this turn-based event.
- `exchange`: The exchange request that the sender cancels.
- `match`: The match related to this turn-based event.

## See Also

- [func player(GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md)
  Handles when the local player receives an exchange request from another participant.
- [func player(GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md)
  Handles when all recipients of an exchange request respond.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:))*