# loadCategories(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads the list of leaderboard categories along with their corresponding localized titles.

**Availability**:
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func loadCategories() async throws -> ([String], [String])
```

#### Discussion

You use this class method to retrieve the category identifiers and titles you configure for your leaderboards in App Store Connect. To create a leaderboard query that targets a particular category, set the [`category`](gkleaderboard/category.md) property to one of the strings that this method returns.

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task is complete, GameKit calls your completion handler on the main thread.

## Parameters

- `completionHandler`: The block receives the following parameters:

## See Also

- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](gkleaderboard/setdefault(_:withcompletionhandler:).md)
  Sets the default leaderboard for the local player.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](gkleaderboard/loadleaderboards(completionhandler:).md)
  Loads a list of leaderboards from Game Center.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](gkleaderboard/loadscores(completionhandler:).md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadcategories(completionhandler:))*