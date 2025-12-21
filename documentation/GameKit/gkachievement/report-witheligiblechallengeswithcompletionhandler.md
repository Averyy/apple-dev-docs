# report(_:withEligibleChallenges:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge]) async throws
```

#### Discussion

Call this method to communicate to Game Center about the local player’s progress towards completing one or more achievements.

Game Center only updates the achievement’s [`percentComplete`](gkachievement/percentcomplete.md) and [`lastReportedDate`](gkachievement/lastreporteddate.md) properties if the [`percentComplete`](gkachievement/percentcomplete.md) property of an achievement that you pass to this method is greater than the current value. If the achievement is hidden, Game Center also makes it visible. If the [`percentComplete`](gkachievement/percentcomplete.md) property is `100.0`, Game Center sets its [`isCompleted`](gkachievement/iscompleted.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) and may show a banner to the player.

For efficiency, include multiple achievements rather than invoking this method separately for each achievement. Since Game Center associates an achievement with the local player at the time you create the achievement, only invoke this method after you initialize the same player on the device.

## Parameters

- `achievements`: The achievements that you’re reporting to Game Center.
- `challenges`: The limited challenges associated with the achievements.
- `completionHandler`: The block receives the following parameter:

## See Also

- [class func report([GKAchievement], withCompletionHandler: (((any Error)?) -> Void)?)](gkachievement/report(_:withcompletionhandler:).md)
  Reports the player’s progress of players toward one or more achievements.
- [var showsCompletionBanner: Bool](gkachievement/showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](gkachievement/resetachievements(completionhandler:).md)
  Resets the percentage completed for all of the player’s achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/report(_:witheligiblechallenges:withcompletionhandler:))*