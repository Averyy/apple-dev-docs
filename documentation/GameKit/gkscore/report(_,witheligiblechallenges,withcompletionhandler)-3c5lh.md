# report(_:withEligibleChallenges:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Submits a list of scores and all eligible challenges.

**Availability**:
- iOS 6.0+ - Deprecated in 14.0
- iPadOS 6.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.10+ - Deprecated in 11.0
- tvOS - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func report(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func report(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge]) async throws
```

```objc
+ (void) reportScores:(NSArray<GKScore *> *) scores withEligibleChallenges:(NSArray<GKChallenge *> *) challenges withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `scores`: An array of scores to report.
- `challenges`: An array of challenges that GameKit associates with the reported scores.
- `completionHandler`: A block that GameKit calls when the download completes.

  The block receives the following parameter:

  - ***error***: If an error occurred, this object describes the error. If the operation completed successfully, this value is `nil`.

## See Also

### Reporting a New Score
- [class func report([GKLeaderboardScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29-2tycl.md)
  Submits a list of scores and all eligible challenges.
- [class func report([GKScore], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,withcompletionhandler%29.md)
  Reports a list of scores to Game Center


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-3c5lh)*