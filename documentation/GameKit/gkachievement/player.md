# player

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player who earned the achievement.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var player: GKPlayer { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) GKPlayer * player;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) GKPlayer * player;
```

## See Also

### Accessing Achievement Properties
- [var identifier: String](./identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var percentComplete: Double](./percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
- [var lastReportedDate: Date](./lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/player)*