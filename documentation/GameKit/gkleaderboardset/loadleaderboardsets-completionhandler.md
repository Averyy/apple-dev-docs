# loadLeaderboardSets(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads all of the leaderboard sets you configure for your game.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func loadLeaderboardSets() async throws -> [GKLeaderboardSet]
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkleaderboardset/loadimage(completionhandler:).md)
  Loads the localized image that you associate with the leaderboard set.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkleaderboardset/loadleaderboards(handler:).md)
  Loads the leaderboards in the leaderboard set.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboards(completionhandler:).md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadleaderboardsets(completionhandler:))*