# isCompleted

**Framework**: GameKit  
**Kind**: property

A Boolean value that states whether the player has completed the achievement.

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
var isCompleted: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/swift/true) if the `percentComplete` property is equal to `100.0`; otherwise, it’s [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var identifier: String](gkachievement/identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var player: GKPlayer](gkachievement/player.md)
  The player who earned the achievement.
- [var percentComplete: Double](gkachievement/percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var lastReportedDate: Date](gkachievement/lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/iscompleted)*