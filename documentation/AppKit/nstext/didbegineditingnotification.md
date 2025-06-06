# didBeginEditingNotification

**Framework**: AppKit  
**Kind**: property

Posted when an `NSText` object begins any operation that changes characters or formatting attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didBeginEditingNotification: NSNotification.Name
```

#### Discussion

The notification object is the notifying `NSText` object. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let didChangeNotification: NSNotification.Name](nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let didEndEditingNotification: NSNotification.Name](nstext/didendeditingnotification.md)
  Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.
- [class let movementUserInfoKey: String](nstext/movementuserinfokey.md)
  The `userInfo` dictionary key for the [`didEndEditingNotification`](nstext/didendeditingnotification.md) notification.
- [enum NSTextMovement](nstextmovement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/didbegineditingnotification)*