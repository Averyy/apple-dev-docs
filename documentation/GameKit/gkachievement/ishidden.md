# isHidden

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system hides this achievement from the player.

**Availability**:
- iOS 4.1+ - Deprecated in 6.0
- iPadOS 4.1+ - Deprecated in 6.0
- Mac Catalyst 4.1+ - Deprecated in 6.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`isHidden`](../gkachievementdescription/ishidden.md) property on the [`GKAchievementDescription`](../gkachievementdescription.md) class instead.

## Declaration

```swift
var isHidden: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly, getter=isHidden) BOOL hidden;
```

*macOS*

```objc
@property (atomic, assign, readonly, getter=isHidden) BOOL hidden;
```

## See Also

### Deprecated Properties
- [var playerID: String?](./playerid.md)
  A string that identifies the player who earned the achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievement/ishidden)*