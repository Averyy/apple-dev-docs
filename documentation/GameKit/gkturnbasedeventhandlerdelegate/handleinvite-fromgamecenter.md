# handleInvite(fromGameCenter:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Sent to the delegate when the local player receives an invitation to join a new turn-based match.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func handleInvite(fromGameCenter playersToInvite: [String])
```

#### Discussion

When your delegate receives this message, your game should create a new [`GKMatchRequest`](gkmatchrequest.md) object and assign the `playersToInvite` parameter to the match request’s [`playersToInvite`](gkmatchrequest/playerstoinvite.md) property. Then, your game can either call the [`GKTurnBasedMatch`](gkturnbasedmatch.md) class method [`find(for:withCompletionHandler:)`](gkturnbasedmatch/find(for:withcompletionhandler:).md) to find a match programmatically or it can use the request to instantiate a new [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) object to show a user interface to the player.

## Parameters

- `playersToInvite`: An array of   objects containing the player identifiers for the players to initially invite to the game.

## See Also

- [func handleTurnEvent(for: GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handleturnevent(for:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventhandlerdelegate/handleturnevent(for:didbecomeactive:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handlematchended(_:).md)
  Sent to the delegate when a match the local player is participating in has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:))*