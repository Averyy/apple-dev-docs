# inviter

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The identifier for the player who sends the invitation.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`sender`](./sender.md) property instead.

## Declaration

```swift
var inviter: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, readonly) NSString * inviter;
```

*macOS*

```objc
@property (atomic, retain, readonly) NSString * inviter;
```

## See Also

### Getting Properties
- [var sender: GKPlayer](./sender.md)
  The player who sends the invitation.
- [var playerAttributes: UInt32](./playerattributes.md)
  The player attributes for the match.
- [var playerGroup: Int](./playergroup.md)
  The player group for the match.
- [var isHosted: Bool](./ishosted.md)
  A Boolean value that indicates whether you host the game on your own servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinvite/inviter)*