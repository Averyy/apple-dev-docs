# report(_:withEligibleChallenges:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Submits a list of scores and all eligible challenges.

**Availability**:
- iOS 14.0+ - Deprecated in 26.0
- iPadOS 14.0+ - Deprecated in 26.0
- Mac Catalyst 14.0+ - Deprecated in 26.0
- macOS 11.0+ - Deprecated in 26.0
- tvOS 14.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
class func report(_ scores: [GKLeaderboardScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func report(_ scores: [GKLeaderboardScore], withEligibleChallenges challenges: [GKChallenge]) async throws
```

```objc
+ (void) reportLeaderboardScores:(NSArray<GKLeaderboardScore *> *) scores withEligibleChallenges:(NSArray<GKChallenge *> *) challenges withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `scores`: An array of scores to report.
- `challenges`: An array of challenges that GameKit associates with the reported scores.
- `completionHandler`: A block that GameKit calls when this method completes.

  The block receives the following parameter:

  - ***error***: If an error occurs, this object describes the error. If the operation completed successfully, this value is `nil`.

## See Also

### Reporting a New Score
- [class func report([GKScore], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,withcompletionhandler%29.md)
  Reports a list of scores to Game Center
- [class func report([GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29-3c5lh.md)
  Submits a list of scores and all eligible challenges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-2tycl)*