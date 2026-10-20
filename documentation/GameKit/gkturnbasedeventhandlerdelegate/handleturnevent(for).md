# handleTurnEvent(for:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when it is the local player’s turn to act in a turn-based match.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Implement [`handleTurnEvent(for:didBecomeActive:)`](./handleturnevent%28for,didbecomeactive%29.md) instead.

## Declaration

```swift
optional func handleTurnEvent(for match: GKTurnBasedMatch)
```

```objc
- (void) handleTurnEventForMatch:(GKTurnBasedMatch *) match;
```

#### Discussion

When your delegate receives this message, the player has accepted a push notification for a match already in progress. Your game should end whatever task it was performing and switch to the match information provided by the match object.

## Parameters

- `match`: A match object containing the current state of the match.

## See Also

### Receiving Turn-based Events
- [func handleInvite(fromGameCenter: [String])](./handleinvite%28fromgamecenter%29.md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](./handleturnevent%28for,didbecomeactive%29.md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](./handlematchended%28_%29.md)
  Sent to the delegate when a match the local player is participating in has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handleturnevent(for:))*