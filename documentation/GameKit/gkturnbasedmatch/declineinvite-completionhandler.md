# declineInvite(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Declines an invitation for the local player to join a turn-based match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func declineInvite() async throws
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

When you provide a custom interface for managing matches, use this method to programmatically decline an invitation on behalf of the local player.

## Parameters

- `completionHandler`: The block receives the following parameter:

## See Also

- [class func find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, (any Error)?) -> Void)](gkturnbasedmatch/find(for:withcompletionhandler:).md)
  Creates a new match or finds an existing match that needs a player.
- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/acceptinvite(completionhandler:).md)
  Accepts an invitation for the local player to join a turn-based match.
- [func rematch(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/rematch(completionhandler:).md)
  Creates a new turn-based match with the same participants from an existing match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/declineinvite(completionhandler:))*