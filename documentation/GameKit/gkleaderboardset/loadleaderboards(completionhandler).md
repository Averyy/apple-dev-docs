# loadLeaderboards(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads all of the leaderboards for the current leaderboard set.

**Availability**:
- iOS 7.0+ - Deprecated in 14.0
- iPadOS 7.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: Use [`loadLeaderboards(handler:)`](./loadleaderboards%28handler%29.md) instead.

## Declaration

```swift
func loadLeaderboards(completionHandler: (@Sendable ([GKLeaderboard]?, (any Error)?) -> Void)? = nil)
```

```swift
func loadLeaderboards() async throws -> [GKLeaderboard]
```

```objc
- (void) loadLeaderboardsWithCompletionHandler:(void (^)(NSArray<GKLeaderboard *> *leaderboards, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block that this method calls when it loads the leaderboards.

  The block receives the following parameters:

  - ***leaderboards***: An array of `GKLeaderboard` objects that provides the leaderboards for your game.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboard Sets
- [func loadImage(completionHandler: ((UIImage?, (any Error)?) -> Void)?)](./loadimage%28completionhandler%29.md)
  Loads the localized image that you associate with the leaderboard set.
- [class func loadLeaderboardSets(completionHandler: (([GKLeaderboardSet]?, (any Error)?) -> Void)?)](./loadleaderboardsets%28completionhandler%29.md)
  Loads all of the leaderboard sets you configure for your game.
- [func loadLeaderboards(handler: ([GKLeaderboard]?, (any Error)?) -> Void)](./loadleaderboards%28handler%29.md)
  Loads the leaderboards in the leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardset/loadleaderboards(completionhandler:))*