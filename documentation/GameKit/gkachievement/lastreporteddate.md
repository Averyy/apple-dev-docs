# lastReportedDate

**Framework**: GameKit  
**Kind**: property

The last time your game reported progress on the achievement for the player.

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
var lastReportedDate: Date { get }
```

#### Discussion

GameKit initializes this property to the current date.

## See Also

- [var identifier: String](gkachievement/identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var player: GKPlayer](gkachievement/player.md)
  The player who earned the achievement.
- [var percentComplete: Double](gkachievement/percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var isCompleted: Bool](gkachievement/iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/lastreporteddate)*