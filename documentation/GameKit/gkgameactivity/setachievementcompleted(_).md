# setAchievementCompleted(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Set progress to 100% for an achievement for a player.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setAchievementCompleted(_ achievement: GKAchievement)
```

```objc
- (void) setAchievementCompleted:(GKAchievement *) achievement;
```

## Discussion

The system reports achievement completion when the activity ends.

## See Also

### Getting and removing achievements
- [var achievements: Set<GKAchievement>](./achievements.md)
  All achievements that have been associated with this activity.
- [func removeAchievements([GKAchievement])](./removeachievements%28_%29.md)
  Removes all achievements if they exist.
- [func progress(on: GKAchievement) -> Double](./progress%28on%29.md)
  Get the achievement progress from a specific achievement of the local player if previously set.
- [func setProgress(on: GKAchievement, to: Double)](./setprogress%28on,to%29.md)
  Set a progress for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/setachievementcompleted(_:))*