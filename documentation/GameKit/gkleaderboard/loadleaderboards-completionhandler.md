# loadLeaderboards(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads a list of leaderboards from Game Center.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func loadLeaderboards() async throws -> [GKLeaderboard]
```

#### Discussion

Use this class method to retrieve the list of leaderboards you configure in App Store Connect. Use the properties of each leaderboard object, especially the [`category`](gkleaderboard/category.md) and [`title`](gkleaderboard/title.md) properties, to learn more about the leaderboard.

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

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](gkleaderboard/setdefault(_:withcompletionhandler:).md)
  Sets the default leaderboard for the local player.
- [class func loadCategories(completionHandler: (([String]?, [String]?, (any Error)?) -> Void)?)](gkleaderboard/loadcategories(completionhandler:).md)
  Loads the list of leaderboard categories along with their corresponding localized titles.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](gkleaderboard/loadscores(completionhandler:).md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadleaderboards(completionhandler:))*