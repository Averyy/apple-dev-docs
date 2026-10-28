# isCompleted

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isCompleted) BOOL completed;
```

*macOS*

```objc
@property (atomic, readonly, getter=isCompleted) BOOL completed;
```

## Discussion

This property is [`true`](../../Swift/true.md) if the `percentComplete` property is equal to `100.0`; otherwise, it’s [`false`](../../Swift/false.md).

## See Also

### Accessing Achievement Properties
- [var identifier: String](./identifier.md)
  The identifier for the achievement that you enter in App Store Connect.
- [var player: GKPlayer](./player.md)
  The player who earned the achievement.
- [var percentComplete: Double](./percentcomplete.md)
  A percentage value that states how far the player has progressed on the achievement.
- [var lastReportedDate: Date](./lastreporteddate.md)
  The last time your game reported progress on the achievement for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/iscompleted)*