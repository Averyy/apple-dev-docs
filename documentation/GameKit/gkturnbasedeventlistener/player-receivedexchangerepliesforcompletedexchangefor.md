# player(_:receivedExchangeReplies:forCompletedExchange:for:)

**Framework**: GameKit  
**Kind**: method

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

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

GameKit sends this turn-based event to the current participant and the participant who initiates the exchange request.

If your game isn’t running or is in the background on participant devices, a notification containing the localized message you provide appears. When the participant taps or clicks the notification, GameKit launches or brings the game to the foreground and then invokes the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `replies`: The replies from other participants to the exchange request.
- `exchange`: The exchange request that the recipients reply to.
- `match`: The match related to this turn-based event.

## See Also

- [func player(GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md)
  Handles when the local player receives an exchange request from another participant.
- [func player(GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md)
  Handles when the sender cancels an exchange request they intiated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:))*