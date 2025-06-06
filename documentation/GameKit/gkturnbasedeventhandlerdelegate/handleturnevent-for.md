# handleTurnEvent(for:)

**Framework**: GameKit  
**Kind**: method

Sent to the delegate when it is the local player’s turn to act in a turn-based match.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func handleTurnEvent(for match: GKTurnBasedMatch)
```

#### Discussion

When your delegate receives this message, the player has accepted a push notification for a match already in progress. Your game should end whatever task it was performing and switch to the match information provided by the match object.

## Parameters

- `match`: A match object containing the current state of the match.

## See Also

- [func handleInvite(fromGameCenter: [String])](gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:).md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventhandlerdelegate/handleturnevent(for:didbecomeactive:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handlematchended(_:).md)
  Sent to the delegate when a match the local player is participating in has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handleturnevent(for:))*