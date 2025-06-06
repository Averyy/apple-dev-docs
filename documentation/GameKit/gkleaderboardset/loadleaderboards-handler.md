# loadLeaderboards(handler:)

**Framework**: GameKit  
**Kind**: method

Loads the leaderboards in the leaderboard set.

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
func loadLeaderboards(handler: @escaping ([GKLeaderboard]?, (any Error)?) -> Void)
```

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `handler`: The block receives the following parameters:

## See Also

- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](gkleaderboardset/loadimage(completionhandler:).md)
  Loads the localized image that you associate with the leaderboard set.
- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboardsets(completionhandler:).md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboards(completionhandler:).md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadleaderboards(handler:))*