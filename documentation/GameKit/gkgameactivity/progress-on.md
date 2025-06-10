# progress(on:)

**Framework**: GameKit  
**Kind**: method

Get the achievement progress from a specific achievement of the local player if previously set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func progress(on achievement: GKAchievement) -> Double
```

#### Discussion

Returns 0 if the achievement has not been set in the current activity.

## See Also

- [var achievements: Set<GKAchievement>](gkgameactivity/achievements.md)
  All achievements that have been associated with this activity.
- [func removeAchievements([GKAchievement])](gkgameactivity/removeachievements(_:).md)
  Removes all achievements if exist.
- [func setProgress(on: GKAchievement, to: Double)](gkgameactivity/setprogress(on:to:).md)
  Set a progress for an achievement for a player.
- [func setAchievementCompleted(GKAchievement)](gkgameactivity/setachievementcompleted(_:).md)
  Convenience method to set a progress to 100% for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/progress(on:))*