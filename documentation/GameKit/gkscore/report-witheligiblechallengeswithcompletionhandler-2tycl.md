# report(_:withEligibleChallenges:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Submits a list of scores and all eligible challenges.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func report(_ scores: [GKLeaderboardScore], withEligibleChallenges challenges: [GKChallenge]) async throws
```

## Parameters

- `scores`: An array of scores to report.
- `challenges`: An array of challenges that GameKit associates with the reported scores.
- `completionHandler`: The block receives the following parameter:

## See Also

- [class func report([GKScore], withCompletionHandler: (((any Error)?) -> Void)?)](gkscore/report(_:withcompletionhandler:).md)
  Reports a list of scores to Game Center
- [class func report([GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-3c5lh.md)
  Submits a list of scores and all eligible challenges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-2tycl)*