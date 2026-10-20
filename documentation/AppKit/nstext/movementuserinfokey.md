# movementUserInfoKey

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The `userInfo` dictionary key for the [`didEndEditingNotification`](./didendeditingnotification.md) notification.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class let movementUserInfoKey: String
```

```c
extern NSString * const NSTextMovementUserInfoKey;
```

## See Also

### Notifications
- [class let didBeginEditingNotification: NSNotification.Name](./didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](./didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](./didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [enum NSTextMovement](../nstextmovement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/movementuserinfokey)*