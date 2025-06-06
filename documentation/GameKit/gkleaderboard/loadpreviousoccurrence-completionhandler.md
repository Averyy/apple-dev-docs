# loadPreviousOccurrence(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the previous recurring leaderboard occurrence that the player submits a score to.

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
func loadPreviousOccurrence() async throws -> GKLeaderboard?
```

## Mentions

- [Creating recurring leaderboards](creating-recurring-leaderboards.md)
- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func loadLeaderboards(IDs: [String]?, completionHandler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkleaderboard/loadleaderboards(ids:completionhandler:).md)
  Loads leaderboards for the specified leaderboard IDs that Game Center uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadpreviousoccurrence(completionhandler:))*