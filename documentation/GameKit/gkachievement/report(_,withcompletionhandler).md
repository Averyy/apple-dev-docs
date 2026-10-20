# report(_:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Reports the player’s progress of players toward one or more achievements.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func report(_ achievements: [GKAchievement], withCompletionHandler completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func report(_ achievements: [GKAchievement]) async throws
```

```objc
+ (void) reportAchievements:(NSArray<GKAchievement *> *) achievements withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Rewarding players with achievements](../rewarding-players-with-achievements.md)

#### Discussion

Call this method to communicate to Game Center about the local player’s progress towards completing one or more achievements.

Game Center only updates the achievement’s [`percentComplete`](./percentcomplete.md) and [`lastReportedDate`](./lastreporteddate.md) properties if the [`percentComplete`](./percentcomplete.md) property of an achievement that you pass to this method is greater than the current value. If the achievement is hidden, Game Center also makes it visible. If the [`percentComplete`](./percentcomplete.md) property is `100.0`, Game Center sets its [`isCompleted`](./iscompleted.md) property to [`true`](../../Swift/true.md) and may show a banner to the player.

For efficiency, include multiple achievements rather than invoking this method separately for each achievement. Since Game Center associates an achievement with the local player at the time you create the achievement, only invoke this method after you initialize the same player on the device.

## Parameters

- `achievements`: The achievements that you’re reporting to Game Center.
- `completionHandler`: A block that GameKit calls when the operation completes.

  The block receives the following parameter:

  - **`error`**: Describes an error if it occurs, or `nil` if the operation completes.

## See Also

### Reporting Progress on Achievements
- [class func report([GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](./report%28_,witheligiblechallenges,withcompletionhandler%29.md)
  Reports the player’s progress on achievements and limits the challenges, associated with those achievements, that the player may complete.
- [var showsCompletionBanner: Bool](./showscompletionbanner.md)
  A Boolean value that indicates whether GameKit displays a banner when the player completes the achievement.
- [class func resetAchievements(completionHandler: (((any Error)?) -> Void)?)](./resetachievements%28completionhandler%29.md)
  Resets the percentage completed for all of the player’s achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/report(_:withcompletionhandler:))*