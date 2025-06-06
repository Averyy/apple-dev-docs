# rematch(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Creates a new turn-based match with the same participants from an existing match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func rematch() async throws -> GKTurnBasedMatch
```

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](gkturnbasedmatch/find(for:withcompletionhandler:).md)
  Creates a new match or finds an existing match that needs a player.
- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/acceptinvite(completionhandler:).md)
  Accepts an invitation for the local player to join a turn-based match.
- [func declineInvite(completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/declineinvite(completionhandler:).md)
  Declines an invitation for the local player to join a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/rematch(completionhandler:))*