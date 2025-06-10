# image

**Framework**: GameKit  
**Kind**: property

The achievement’s artwork that you display when the player completes the achievement.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var image: NSImage? { get }
```

#### Discussion

The value of this property is undefined until you load the image using the [`loadImage(completionHandler:)`](gkachievementdescription/loadimage(completionhandler:).md) method.

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
- [var isHidden: Bool](gkachievementdescription/ishidden.md)
  A Boolean value that states whether the achievement is initially visible to players.
- [var isReplayable: Bool](gkachievementdescription/isreplayable.md)
  A Boolean value that states whether the player can earn the achievement multiple times.
- [var rarityPercent: Double?](gkachievementdescription/raritypercent-4bh6k.md)
  The percentage of players of this game that earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/image)*