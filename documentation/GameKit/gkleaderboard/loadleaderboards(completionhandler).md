# loadLeaderboards(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads a list of leaderboards from Game Center.

**Availability**:
- iOS 6.0+ - Deprecated in 14.0
- iPadOS 6.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use the [`loadLeaderboards(IDs:completionHandler:)`](./loadleaderboards%28ids,completionhandler%29.md) method instead.

## Declaration

```swift
class func loadLeaderboards(completionHandler: (@Sendable ([GKLeaderboard]?, (any Error)?) -> Void)? = nil)
```

```swift
class func loadLeaderboards() async throws -> [GKLeaderboard]
```

```objc
+ (void) loadLeaderboardsWithCompletionHandler:(void (^)(NSArray<GKLeaderboard *> *leaderboards, NSError *error)) completionHandler;
```

#### Discussion

Use this class method to retrieve the list of leaderboards you configure in App Store Connect. Use the properties of each leaderboard object, especially the [`category`](./category.md) and [`title`](./title.md) properties, to learn more about the leaderboard.

```objc
- (void) loadLeaderboardInfo
{
    [GKLeaderboard loadLeaderboardsWithCompletionHandler:^(NSArray *leaderboards, NSError *error) {
        self.leaderboards = leaderboards;
     }];
}
```

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task is complete, GameKit calls your completion handler on the main thread.

## Parameters

- `completionHandler`: A block to call when loading the leaderboards.

  The block receives the following parameters:

  - ***leaderboards***: An array of `GKLeaderboard` objects that provides the leaderboards for your game. If an error occurs, this value may be non-`nil`. In this case, the array holds whatever data GameKit downloads before the error occurs.
  - ***error***: If an error occurs, this error object describes the error. If the operation completes successfully, the value is `nil`.

## See Also

### Deprecated methods
- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](./setdefault%28_,withcompletionhandler%29.md)
  Sets the default leaderboard for the local player.
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](./loadcategories%28completionhandler%29.md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](./loadscores%28completionhandler%29.md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadleaderboards(completionhandler:))*