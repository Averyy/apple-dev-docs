# setDefault(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Sets the default leaderboard for the local player.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`setDefaultLeaderboardIdentifier(_:completionHandler:)`](../gklocalplayer/setdefaultleaderboardidentifier%28_,completionhandler%29.md) method instead.

## Declaration

*macOS, visionOS, watchOS*

```swift
class func setDefault(_ leaderboardIdentifier: String?, withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
class func setDefault(_ leaderboardIdentifier: String?) async throws
```

```objc
+ (void) setDefaultLeaderboard:(NSString *) leaderboardIdentifier withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

GameKit uses the default leaderboard whenever your game uses a [`GKScore`](../gkscore.md) object to report a score to Game Center without explicitly setting the score object’s [`category`](../gkscore/category.md) property. You normally set the default leaderboard in App Store Connect. However, your game can use this class method to override the default leaderboard that appears for the local player. Game Center stores this information for each player.

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task completes, GameKit calls your completion handler on the main thread.

If an error occurs and it’s a network error, periodically resend the request until it completes.

## Parameters

- `leaderboardIdentifier`: The named leaderboard that is the new default leaderboard for the local player.
- `completionHandler`: A block to call after retrieving scores from the server.

  The block receives the following parameter:

  - ***error***: If an error occurs, this error object describes the error. If the operation completes successfully, the value is `nil`.

## See Also

### Deprecated methods
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](./loadcategories%28completionhandler%29.md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads a list of leaderboards from Game Center.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](./loadscores%28completionhandler%29.md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/setdefault(_:withcompletionhandler:))*