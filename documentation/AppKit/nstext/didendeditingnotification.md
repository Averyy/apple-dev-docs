# didEndEditingNotification

**Framework**: Appkit  
**Kind**: property

Posted when focus leaves an `NSText` object, whether or not any operation has changed characters or formatting attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didEndEditingNotification: NSNotification.Name
```

#### Discussion

The notification object is the notifying `NSText` object. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| [`movementUserInfoKey`](nstext/movementuserinfokey.md) | One of the values in [`NSTextMovement`](nstextmovement.md). |

| Key | Value |
| --- | --- |
| `@"NSTextMovement"` | Possible movement code values are described in [`Movement Codes`](movement-codes.md). |

> **Note**:  It is common for [`didEndEditingNotification`](nstext/didendeditingnotification.md) to be sent without a matching [`didBeginEditingNotification`](nstext/didbegineditingnotification.md). The begin notification is only sent if the user actually makes changes (that is, types something or changes formatting attributes). However, the end notification is sent when focus leaves the text view, regardless of whether there was a change. This distinction enables an application to know whether the user actually made a change to the text or just clicked in the text view and then clicked outside it. In both cases, [`didEndEditingNotification`](nstext/didendeditingnotification.md) is sent, but to tell the difference, the application can listen for [`didBeginEditingNotification`](nstext/didbegineditingnotification.md).

## See Also

- [class let didBeginEditingNotification: NSNotification.Name](nstext/didbegineditingnotification.md)
  Posted when an `NSText` object begins any operation that changes characters or formatting attributes.
- [class let didChangeNotification: NSNotification.Name](nstext/didchangenotification.md)
  Posted after an `NSText` object performs any operation that changes characters or formatting attributes.
- [class let movementUserInfoKey: String](nstext/movementuserinfokey.md)
  The `userInfo` dictionary key for the [`didEndEditingNotification`](nstext/didendeditingnotification.md) notification.
- [enum NSTextMovement](nstextmovement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/didendeditingnotification)*