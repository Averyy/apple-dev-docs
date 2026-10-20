# report(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Reports a list of scores to Game Center

**Availability**:
- iOS 6.0+ - Deprecated in 14.0
- iPadOS 6.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.8+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

## Declaration

```swift
class func report(_ scores: [GKScore], withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func report(_ scores: [GKScore]) async throws
```

```objc
+ (void) reportScores:(NSArray<GKScore *> *) scores withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Use this class method whenever you need to submit scores to Game Center, whether you are reporting a single score or multiple scores. The method runs through the array of `GKScore` objects, submitting scores one at a time.

[`report(_:withCompletionHandler:)`](./report%28_,withcompletionhandler%29.md) provides a sample method to report a score. The `GKScore` object is initialized with the leaderboard ID for the leaderboard it reports its score to and then the [`value`](./value.md) and [`context`](./context.md) for the score are assigned. The leaderboard ID must be the identifier for a leaderboard you configured in App Store Connect. Scores are always reported for the current local player and never for friends.

```objc
- (void) reportScore: (int64_t) score forLeaderboardID: (NSString*) identifier
{
    GKScore *scoreReporter = [[GKScore alloc] initWithLeaderboardIdentifier: identifier];
    scoreReporter.value = score;
    scoreReporter.context = 0;
 
    NSArray *scores = @[scoreReporter];
    [GKScore reportScores:scores withCompletionHandler:^(NSError *error) {
    //Do something interesting here.
    }];
}
```

## Parameters

- `scores`: An array of scores to report to Game Center.
- `completionHandler`: A block that GameKit calls when it reports the scores.

  The block receives the following parameter:

  - ***error***: If an error occurred, this parameter holds an error object that describes the problem. If the score was successfully reported, this parameter’s value is `nil`.

## See Also

### Reporting a New Score
- [class func report([GKLeaderboardScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29-2tycl.md)
  Submits a list of scores and all eligible challenges.
- [class func report([GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29-3c5lh.md)
  Submits a list of scores and all eligible challenges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore/report(_:withcompletionhandler:))*