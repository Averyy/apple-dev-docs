# isReplayable

**Framework**: GameKit  
**Kind**: property

A Boolean value that states whether the player can earn the achievement multiple times.

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
var isReplayable: Bool { get }
```

#### Discussion

If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), players can earn the achievement only once. After the player earns the achievement, Game Center ignores any further progress you report for it. If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the player earns the achievement each time you report it.

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
- [var rarityPercent: Double?](gkachievementdescription/raritypercent-4bh6k.md)
  The percentage of players of this game that earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/isreplayable)*