# achievements

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

All achievements that have been associated with this activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var achievements: Set<GKAchievement> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<GKAchievement *> * achievements;
```

#### Discussion

Progress of each achievement will be reported when the activity ends.

## See Also

### Getting and removing achievements
- [func removeAchievements([GKAchievement])](./removeachievements%28_%29.md)
  Removes all achievements if they exist.
- [func progress(on: GKAchievement) -> Double](./progress%28on%29.md)
  Get the achievement progress from a specific achievement of the local player if previously set.
- [func setProgress(on: GKAchievement, to: Double)](./setprogress%28on,to%29.md)
  Set a progress for an achievement for a player.
- [func setAchievementCompleted(GKAchievement)](./setachievementcompleted%28_%29.md)
  Set progress to 100% for an achievement for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/achievements)*