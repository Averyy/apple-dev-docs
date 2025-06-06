# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the localized image that you associate with the leaderboard set.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func loadImage() async throws -> UIImage
```

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboardsets(completionhandler:).md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkleaderboardset/loadleaderboards(handler:).md)
  Loads the leaderboards in the leaderboard set.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboardset/loadleaderboards(completionhandler:).md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadimage(completionhandler:))*