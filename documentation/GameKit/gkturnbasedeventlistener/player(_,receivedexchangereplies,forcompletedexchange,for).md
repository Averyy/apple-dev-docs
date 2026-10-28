# player(_:receivedExchangeReplies:forCompletedExchange:for:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when all recipients of an exchange request respond.

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
optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)
```

```objc
- (void) player:(GKPlayer *) player receivedExchangeReplies:(NSArray<GKTurnBasedExchangeReply *> *) replies forCompletedExchange:(GKTurnBasedExchange *) exchange forMatch:(GKTurnBasedMatch *) match;
```

## Mentions

- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## Discussion

GameKit sends this turn-based event to the current participant and the participant who initiates the exchange request.

If your game isn’t running or is in the background on participant devices, a notification containing the localized message you provide appears. When the participant taps or clicks the notification, GameKit launches or brings the game to the foreground and then invokes the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](./player%28_,receivedexchangereplies,forcompletedexchange,for%29.md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `replies`: The replies from other participants to the exchange request.
- `exchange`: The exchange request that the recipients reply to.
- `match`: The match related to this turn-based event.

## See Also

### Handling Data Exchanges
- [func player(GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangerequest,for%29.md)
  Handles when the local player receives an exchange request from another participant.
- [func player(GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](./player%28_,receivedexchangecancellation,for%29.md)
  Handles when the sender cancels an exchange request they intiated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:))*