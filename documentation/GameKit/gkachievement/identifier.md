# identifier

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The identifier for the achievement that you enter in App Store Connect.

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
var identifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * identifier;
```

## See Also

### Accessing Achievement Properties
- [var player: GKPlayer](./player.md)
  The player who earned the achievement.
- [var percentComplete: Double](./percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value that states whether the player has completed the achievement.
- [var lastReportedDate: Date](./lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/identifier)*