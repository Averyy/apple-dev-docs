# didEndEditingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.

**Availability**:
- macOS

## Declaration

```swift
class let didEndEditingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextDidEndEditingNotification;
```

#### Discussion

The notification object is the notifying `NSText` object. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| [`movementUserInfoKey`](./movementuserinfokey.md) | One of the values in [`NSTextMovement`](../nstextmovement.md). |

| Key | Value |
| --- | --- |
| `@"NSTextMovement"` | Possible movement code values are described in [Movement Codes](../movement-codes.md). |

> **Note**:  It is common for [`didEndEditingNotification`](./didendeditingnotification.md) to be sent without a matching [`didBeginEditingNotification`](./didbegineditingnotification.md). The begin notification is only sent if the user actually makes changes (that is, types something or changes formatting attributes). However, the end notification is sent when focus leaves the text view, regardless of whether there was a change.
>
> This distinction enables an application to know whether the user actually made a change to the text or just clicked in the text view and then clicked outside it. In both cases, [`didEndEditingNotification`](./didendeditingnotification.md) is sent, but to tell the difference, the application can listen for [`didBeginEditingNotification`](./didbegineditingnotification.md).

To observe this notification using Swift concurrency, use [`NSTextView.DidEndEditingMessage`](../nstextview/didendeditingmessage.md).

## See Also

### Notifications
- [class let didBeginEditingNotification: NSNotification.Name](./didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](./didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let movementUserInfoKey: String](./movementuserinfokey.md)
  The `userInfo` dictionary key for the [`didEndEditingNotification`](./didendeditingnotification.md) notification.
- [enum NSTextMovement](../nstextmovement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/didendeditingnotification)*