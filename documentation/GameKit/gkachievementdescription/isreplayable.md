# isReplayable

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readonly, getter=isReplayable) BOOL replayable;
```

#### Discussion

If the value of this property is [`false`](../../Swift/false.md), players can earn the achievement only once. After the player earns the achievement, Game Center ignores any further progress you report for it. If the value of this property is [`true`](../../Swift/true.md), the player earns the achievement each time you report it.

## See Also

### Reading and Writing Achievement Properties
- [var identifier: String](./identifier.md)
  The string you enter in App Store Connect that uniquely identifies the achievement.
- [var title: String](./title.md)
  A localized title for the achievement.
- [var unachievedDescription: String](./unachieveddescription.md)
  A localized description of the achievement that you display when the player hasn’t completed the achievement.
- [var achievedDescription: String](./achieveddescription.md)
  A localized description of the achievement that you display when the player completes the achievement.
- [var maximumPoints: Int](./maximumpoints.md)
  The number of points that the player earns when completing the achievement.
- [var image: NSImage?](./image.md)
  The achievement’s artwork that you display when the player completes the achievement.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that states whether the achievement is initially visible to players.
- [var rarityPercent: Double?](./raritypercent-4bh6k.md)
  The percentage of players of this game that earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/isreplayable)*