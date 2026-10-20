# progress(on:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Get the achievement progress from a specific achievement of the local player if previously set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func progress(on achievement: GKAchievement) -> Double
```

```objc
- (double) getProgressOnAchievement:(GKAchievement *) achievement;
```

#### Discussion

Returns `0` if the achievement hasn’t been set in the current activity.

## See Also

### Getting and removing achievements
- [var achievements: Set<GKAchievement>](./achievements.md)
  All achievements that have been associated with this activity.
- [func removeAchievements([GKAchievement])](./removeachievements%28_%29.md)
  Removes all achievements if they exist.
- [func setProgress(on: GKAchievement, to: Double)](./setprogress%28on,to%29.md)
  Set a progress for an achievement for a player.
- [func setAchievementCompleted(GKAchievement)](./setachievementcompleted%28_%29.md)
  Set progress to 100% for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/progress(on:))*