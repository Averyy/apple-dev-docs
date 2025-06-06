# rarityPercent

**Framework**: GameKit  
**Kind**: property

The percentage of players of this game that earned the achievement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var rarityPercent: Double? { get }
```

#### Discussion

The rarity percentage ranges between `0.0` and `100.0`, inclusive, where `0.0` indicates that no player has earned the achievement, and `100.0` indicates that every player has earned the achievement. This property is `nil` if there isn’t enough data to compute the rarity of the achievement.

## See Also

- [var identifier: String](gkachievementdescription/identifier.md)
  The string you enter in App Store Connect that uniquely identifies the achievement.
- [var title: String](gkachievementdescription/title.md)
  A localized title for the achievement.
- [var unachievedDescription: String](gkachievementdescription/unachieveddescription.md)
  A localized description of the achievement that you display when the player hasn’t completed the achievement.
- [var achievedDescription: String](gkachievementdescription/achieveddescription.md)
  A localized description of the achievement that you display when the player completes the achievement.
- [var maximumPoints: Int](gkachievementdescription/maximumpoints.md)
  The number of points that the player earns when completing the achievement.
- [var image: NSImage?](gkachievementdescription/image.md)
  The achievement’s artwork that you display when the player completes the achievement.
- [var isHidden: Bool](gkachievementdescription/ishidden.md)
  A Boolean value that states whether the achievement is initially visible to players.
- [var isReplayable: Bool](gkachievementdescription/isreplayable.md)
  A Boolean value that states whether the player can earn the achievement multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/raritypercent-4bh6k)*