# loadLeaderboards(IDs:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads leaderboards for the specified leaderboard IDs that Game Center uses.

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
class func loadLeaderboards(IDs leaderboardIDs: [String]?, completionHandler: @escaping @Sendable ([GKLeaderboard]?, (any Error)?) -> Void)
```

```swift
class func loadLeaderboards(IDs leaderboardIDs: [String]?) async throws -> [GKLeaderboard]
```

```objc
+ (void) loadLeaderboardsWithIDs:(NSArray<NSString *> *) leaderboardIDs completionHandler:(void (^)(NSArray<GKLeaderboard *> *leaderboards, NSError *error)) completionHandler;
```

## Mentions

- [Creating recurring leaderboards](../creating-recurring-leaderboards.md)
- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `leaderboardIDs`: An array of leaderboard IDs that Game Center uses.
- `completionHandler`: A block that GameKit calls when this method loads the leaderboards.

  The block receives the following parameters:

  - **leaderboards**: The leaderboards that match the IDs.
  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboards
- [func loadPreviousOccurrence(completionHandler: (GKLeaderboard?, (any Error)?) -> Void)](./loadpreviousoccurrence%28completionhandler%29.md)
  Loads the previous recurring leaderboard occurrence that the player submits a score to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadleaderboards(ids:completionhandler:))*