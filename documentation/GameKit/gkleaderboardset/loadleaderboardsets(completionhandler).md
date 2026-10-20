# loadLeaderboardSets(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

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
class func loadLeaderboardSets(completionHandler: (@Sendable ([GKLeaderboardSet]?, (any Error)?) -> Void)? = nil)
```

```swift
class func loadLeaderboardSets() async throws -> [GKLeaderboardSet]
```

```objc
+ (void) loadLeaderboardSetsWithCompletionHandler:(void (^)(NSArray<GKLeaderboardSet *> *leaderboardSets, NSError *error)) completionHandler;
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: A block that GameKit calls when this method completes the request.

  The block receives the following parameters:

  - ***leaderboardSets***: The leaderboard sets in your game.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboard Sets
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](./loadimage%28completionhandler%29.md)
  Loads the localized image that you associate with the leaderboard set.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](./loadleaderboards%28handler%29.md)
  Loads the leaderboards in the leaderboard set.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadleaderboardsets(completionhandler:))*