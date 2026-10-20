# removeAchievements(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Removes all achievements if they exist.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func removeAchievements(_ achievements: [GKAchievement])
```

```objc
- (void) removeAchievements:(NSArray<GKAchievement *> *) achievements;
```

## See Also

### Getting and removing achievements
- [var achievements: Set<GKAchievement>](./achievements.md)
  All achievements that have been associated with this activity.
- [func progress(on: GKAchievement) -> Double](./progress%28on%29.md)
  Get the achievement progress from a specific achievement of the local player if previously set.
- [func setProgress(on: GKAchievement, to: Double)](./setprogress%28on,to%29.md)
  Set a progress for an achievement for a player.
- [func setAchievementCompleted(GKAchievement)](./setachievementcompleted%28_%29.md)
  Set progress to 100% for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/removeachievements(_:))*