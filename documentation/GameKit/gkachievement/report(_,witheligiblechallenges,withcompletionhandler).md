# report(_:withEligibleChallenges:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge]) async throws
```

```objc
+ (void) reportAchievements:(NSArray<GKAchievement *> *) achievements withEligibleChallenges:(NSArray<GKChallenge *> *) challenges withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

Call this method to communicate to Game Center about the local player’s progress towards completing one or more achievements.

Game Center only updates the achievement’s [`percentComplete`](./percentcomplete.md) and [`lastReportedDate`](./lastreporteddate.md) properties if the [`percentComplete`](./percentcomplete.md) property of an achievement that you pass to this method is greater than the current value. If the achievement is hidden, Game Center also makes it visible. If the [`percentComplete`](./percentcomplete.md) property is `100.0`, Game Center sets its [`isCompleted`](./iscompleted.md) property to [`true`](../../Swift/true.md) and may show a banner to the player.

For efficiency, include multiple achievements rather than invoking this method separately for each achievement. Since Game Center associates an achievement with the local player at the time you create the achievement, only invoke this method after you initialize the same player on the device.

## Parameters

- `achievements`: The achievements that you’re reporting to Game Center.
- `challenges`: The limited challenges associated with the achievements.
- `completionHandler`: A block that GameKit calls when this method completes.

  The block receives the following parameter:

  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Reporting Progress on Achievements
- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,withcompletionhandler%29.md)
  Reports the player’s progress of players toward one or more achievements.
- [var showsCompletionBanner: Bool](./showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](./resetachievements%28completionhandler%29.md)
  Resets the percentage completed for all of the player’s achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/report(_:witheligiblechallenges:withcompletionhandler:))*