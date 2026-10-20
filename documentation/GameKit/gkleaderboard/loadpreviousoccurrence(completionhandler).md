# loadPreviousOccurrence(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the previous recurring leaderboard occurrence that the player submits a score to.

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
func loadPreviousOccurrence(completionHandler: @escaping @Sendable (GKLeaderboard?, (any Error)?) -> Void)
```

```swift
func loadPreviousOccurrence() async throws -> GKLeaderboard?
```

```objc
- (void) loadPreviousOccurrenceWithCompletionHandler:(void (^)(GKLeaderboard *leaderboard, NSError *error)) completionHandler;
```

## Mentions

- [Creating recurring leaderboards](../creating-recurring-leaderboards.md)
- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Parameters

- `completionHandler`: A block that GameKit calls when this method loads the leaderboard.

  The block receives the following parameters:

  - **leaderboard**: The previous occurrence of this leaderboard that the player submits a score to, or the most recent occurrence if GameKit can’t find the previous one.
  - **error**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Loading Leaderboards
- [class func loadLeaderboards(IDs: [String]?, completionHandler: ([GKLeaderboard]?, (any Error)?) -> Void)](./loadleaderboards%28ids,completionhandler%29.md)
  Loads leaderboards for the specified leaderboard IDs that Game Center uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/loadpreviousoccurrence(completionhandler:))*