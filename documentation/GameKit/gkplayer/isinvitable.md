# isInvitable

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the local player can send an invitation to the player.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isInvitable: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL isInvitable;
```

*macOS*

```objc
@property (atomic, readonly) BOOL isInvitable;
```

## See Also

### Accessing player details
- [var alias: String](./alias.md)
  A string the player chooses to identify themself to other players.
- [var displayName: String](./displayname.md)
  A string to display for the player.
- [var isFriend: Bool](./isfriend.md)
  A Boolean value that indicates whether the player is a friend of the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/isinvitable)*