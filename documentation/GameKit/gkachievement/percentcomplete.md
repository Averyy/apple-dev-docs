# percentComplete

**Framework**: GameKit  
**Kind**: property

A percentage value that states how far the player has progressed on the achievement.

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
var percentComplete: Double { get set }
```

## Mentions

- [Rewarding players with achievements](rewarding-players-with-achievements.md)

#### Discussion

The default value for a newly initialized achievement object is `0.0`. The range of legal values is between `0.0` and `100.0`, inclusive. You decide how to calculate the percentage and when to change it.

For example, if the player earns an achievement for discovering a location in your game, then you’d report the achievement as 100 percent complete the first time you report progress to Game Center. On the other hand, for an achievement like “Capture 10 pirates”, your reporting mechanism increments by 10 percent each time the player captures a pirate.

## See Also

- [var identifier: String](gkachievement/identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var player: GKPlayer](gkachievement/player.md)
  The player who earned the achievement.
- [var isCompleted: Bool](gkachievement/iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
- [var lastReportedDate: Date](gkachievement/lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/percentcomplete)*