# setDefault(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Sets the default leaderboard for the local player.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func setDefault(_ leaderboardIdentifier: String?) async throws
```

#### Discussion

GameKit uses the default leaderboard whenever your game uses a [`GKScore`](gkscore.md) object to report a score to Game Center without explicitly setting the score object’s [`category`](gkscore/category.md) property. You normally set the default leaderboard in App Store Connect. However, your game can use this class method to override the default leaderboard that appears for the local player. Game Center stores this information for each player.

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task completes, GameKit calls your completion handler on the main thread.

If an error occurs and it’s a network error, periodically resend the request until it completes.

## Parameters

- `leaderboardIdentifier`: The named leaderboard that is the new default leaderboard for the local player.
- `completionHandler`: The block receives the following parameter:

## See Also

- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](gkleaderboard/loadcategories(completionhandler:).md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboard/loadleaderboards(completionhandler:).md)
  Loads a list of leaderboards from Game Center.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](gkleaderboard/loadscores(completionhandler:).md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/setdefault(_:withcompletionhandler:))*