# handleMatchEnded(_:)

**Framework**: GameKit  
**Kind**: method

Sent to the delegate when a match the local player is participating in has ended.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func handleMatchEnded(_ match: GKTurnBasedMatch)
```

#### Discussion

When your delegate receives this message, it should display the match’s final results to the player and allow the player the option of saving or removing the match data from Game Center.

## Parameters

- `match`: The match that just ended.

## See Also

- [func handleInvite(fromGameCenter: [String])](gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:).md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handleturnevent(for:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventhandlerdelegate/handleturnevent(for:didbecomeactive:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handlematchended(_:))*