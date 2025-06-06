# isHidden

**Framework**: GameKit  
**Kind**: property

A Boolean value that states whether the achievement is initially visible to players.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isHidden: Bool { get }
```

#### Discussion

If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the achievement is always visible to the player. If [`true`](https://developer.apple.com/documentation/swift/true), the achievement isn’t displayed in any of the standard achievement user interface screens. It remains hidden until the first time your game reports progress toward completing the achievement.

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
- [var isReplayable: Bool](gkachievementdescription/isreplayable.md)
  A Boolean value that states whether the player can earn the achievement multiple times.
- [var rarityPercent: Double?](gkachievementdescription/raritypercent-4bh6k.md)
  The percentage of players of this game that earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/ishidden)*