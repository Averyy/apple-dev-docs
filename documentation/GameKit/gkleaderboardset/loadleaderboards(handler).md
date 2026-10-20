# loadLeaderboards(handler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) loadLeaderboardsWithHandler:(void (^)(NSArray<GKLeaderboard *> *leaderboards, NSError *error)) handler;
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `handler`: A block that GameKit calls when this method completes the request.

  The block receives the following parameters:

  - ***leaderboards***: The leaderboards in the leaderboard set.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboard Sets
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](./loadimage%28completionhandler%29.md)
  Loads the localized image that you associate with the leaderboard set.
- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](./loadleaderboardsets%28completionhandler%29.md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(completionHandler: (([GKLeaderboard]?, (any Error)?) -> Void)?)](./loadleaderboards%28completionhandler%29.md)
  Loads all of the leaderboards for the current leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadleaderboards(handler:))*