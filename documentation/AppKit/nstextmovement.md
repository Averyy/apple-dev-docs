# NSTextMovement

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSTextMovement
```

## Topics

### Movement Options
- [NSTextMovement.return](nstextmovement/return.md)
- [NSTextMovement.tab](nstextmovement/tab.md)
- [NSTextMovement.backtab](nstextmovement/backtab.md)
- [NSTextMovement.left](nstextmovement/left.md)
- [NSTextMovement.right](nstextmovement/right.md)
- [NSTextMovement.up](nstextmovement/up.md)
- [NSTextMovement.down](nstextmovement/down.md)
- [NSTextMovement.cancel](nstextmovement/cancel.md)
- [NSTextMovement.other](nstextmovement/other.md)
### Initializers
- [init?(rawValue: Int)](nstextmovement/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class let didBeginEditingNotification: NSNotification.Name](nstext/didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](nstext/didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [class let movementUserInfoKey: String](nstext/movementuserinfokey.md)
  The `userInfo` dictionary key for the [`didEndEditingNotification`](nstext/didendeditingnotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextmovement)*