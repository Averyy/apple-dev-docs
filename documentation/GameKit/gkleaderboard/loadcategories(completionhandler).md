# loadCategories(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads the list of leaderboard categories along with their corresponding localized titles.

**Availability**:
- iOS 4.1+ - Deprecated in 6.0
- iPadOS 4.1+ - Deprecated in 6.0
- Mac Catalyst 4.1+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`loadLeaderboards(completionHandler:)`](./loadleaderboards%28completionhandler%29.md) method instead.

## Declaration

*visionOS, watchOS*

```swift
class func loadCategories(completionHandler: (@Sendable ([String]?, [String]?, (any Error)?) -> Void)? = nil)
```

*visionOS*

```swift
class func loadCategories() async throws -> ([String], [String])
```

```objc
+ (void) loadCategoriesWithCompletionHandler:(void (^)(NSArray<NSString *> *categories, NSArray<NSString *> *titles, NSError *error)) completionHandler;
```

## Discussion

You use this class method to retrieve the category identifiers and titles you configure for your leaderboards in App Store Connect. To create a leaderboard query that targets a particular category, set the [`category`](./category.md) property to one of the strings that this method returns.

When you call this method, it creates a new background task to handle the request. The method then returns control to your game. When the task is complete, GameKit calls your completion handler on the main thread.

## Parameters

- `completionHandler`: A block to call after retrieving the categories from the server.

  The block receives the following parameters:

  - ***categories***: An array of `NSString` objects that provides the categories to your game. If an error occurs, this value may be non-`nil`. In this case, the array holds whatever data GameKit downloads before the error occurs.
  - ***titles***: An array of `NSString` objects that provides localized titles for each category. If an error occurs, this value may be non-`nil`. In this case, the array holds whatever data GameKit downloads before the error occurs.
  - ***error***: If an error occurs, this error object describes the error. If the operation completes successfully, the value is `nil`.

## See Also

### Deprecated methods
- [class func setDefault(String?, withCompletionHandler: (((any Error)?) -> Void)?)](./setdefault%28_,withcompletionhandler%29.md)
  Sets the default leaderboard for the local player.
- [class func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads a list of leaderboards from Game Center.
- [func loadScores(completionHandler: (([GKScore]?, (any Error)?) -> Void)?)](./loadscores%28completionhandler%29.md)
  Retrieves a set of scores from Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadcategories(completionhandler:))*