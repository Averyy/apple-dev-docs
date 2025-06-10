# loadLeaderboards(IDs:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads leaderboards for the specified leaderboard IDs that Game Center uses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func loadLeaderboards(IDs leaderboardIDs: [String]?) async throws -> [GKLeaderboard]
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)
- [Creating recurring leaderboards](creating-recurring-leaderboards.md)

## Parameters

- `leaderboardIDs`: An array of leaderboard IDs that Game Center uses.
- `completionHandler`: The block receives the following parameters:

## See Also

- [func loadPreviousOccurrence(completionHandler: (GKLeaderboard?, (any Error)?) -> Void)](gkleaderboard/loadpreviousoccurrence(completionhandler:).md)
  Loads the previous recurring leaderboard occurrence that the player submits a score to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadleaderboards(ids:completionhandler:))*