# setProgress(on:to:)

**Framework**: GameKit  
**Kind**: method

Set a progress for an achievement for a player.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setProgress(on achievement: GKAchievement, to percentComplete: Double)
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

Achievement progress will be reported when the activity ends.

## See Also

- [var achievements: Set<GKAchievement>](gkgameactivity/achievements.md)
  All achievements that have been associated with this activity.
- [func removeAchievements([GKAchievement])](gkgameactivity/removeachievements(_:).md)
  Removes all achievements if exist.
- [func progress(on: GKAchievement) -> Double](gkgameactivity/progress(on:).md)
  Get the achievement progress from a specific achievement of the local player if previously set.
- [func setAchievementCompleted(GKAchievement)](gkgameactivity/setachievementcompleted(_:).md)
  Convenience method to set a progress to 100% for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/setprogress(on:to:))*