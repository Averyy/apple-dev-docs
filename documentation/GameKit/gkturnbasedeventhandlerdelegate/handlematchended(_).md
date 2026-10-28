# handleMatchEnded(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when a match the local player is participating in has ended.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
optional func handleMatchEnded(_ match: GKTurnBasedMatch)
```

```objc
- (void) handleMatchEnded:(GKTurnBasedMatch *) match;
```

## Discussion

When your delegate receives this message, it should display the match’s final results to the player and allow the player the option of saving or removing the match data from Game Center.

## Parameters

- `match`: The match that just ended.

## See Also

### Receiving Turn-based Events
- [func handleInvite(fromGameCenter: [String])](./handleinvite%28fromgamecenter%29.md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch)](./handleturnevent%28for%29.md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](./handleturnevent%28for,didbecomeactive%29.md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handlematchended(_:))*