# find(for:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Creates a new match or finds an existing match that needs a player.

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
class func find(for request: GKMatchRequest) async throws -> GKTurnBasedMatch
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

When you provide a custom interface for managing matches, use this method to programmatically create or find a turn-based match on behalf of the local player. The local player is always the current participant in the match object GameKit passes to the completion handler. Therefore, implement the completion handler to show the gameplay interface and let the local player take their turn.

To be consistent with older servers and earlier versions of iOS, GameKit sets the minimum number of players specified by the `GKMatchRequest` object to be equal to the maximum number of players when looking for a match.

## Parameters

- `request`: The configuration for the turn-based match.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func acceptInvite(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/acceptinvite(completionhandler:).md)
  Accepts an invitation for the local player to join a turn-based match.
- [func declineInvite(completionHandler: (((any Error)?) -> Void)?)](gkturnbasedmatch/declineinvite(completionhandler:).md)
  Declines an invitation for the local player to join a turn-based match.
- [func rematch(completionHandler: ((GKTurnBasedMatch?, (any Error)?) -> Void)?)](gkturnbasedmatch/rematch(completionhandler:).md)
  Creates a new turn-based match with the same participants from an existing match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/find(for:withcompletionhandler:))*