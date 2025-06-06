# handleTurnEvent(for:didBecomeActive:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Sent to the delegate when it is the local player’s turn to act in a turn-based match.

**Availability**:
- macOS 10.9+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func handleTurnEvent(for match: GKTurnBasedMatch, didBecomeActive: Bool)
```

#### Discussion

When your delegate receives this message, the player has accepted a push notification for a match already in progress. Your game should end whatever task it was performing and switch to the match information provided by the match object.

## Parameters

- `match`: A match object containing the current state of the match.
- `didBecomeActive`:   if the game was launched or brought to the foreground to handle the event.

## See Also

- [func handleInvite(fromGameCenter: [String])](gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:).md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handleturnevent(for:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handlematchended(_:).md)
  Sent to the delegate when a match the local player is participating in has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handleturnevent(for:didbecomeactive:))*