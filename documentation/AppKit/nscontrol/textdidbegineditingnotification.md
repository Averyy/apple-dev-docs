# textDidBeginEditingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent when a control with editable cells begins an edit session.

**Availability**:
- macOS

## Declaration

```swift
class let textDidBeginEditingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSControlTextDidBeginEditingNotification;
```

#### Discussion

The field editor of the edited cell originally sends an [`didBeginEditingNotification`](../nstext/didbegineditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [`controlTextDidEndEditing:`](../../ObjectiveC/nsobject-swift.class/controltextdidendediting_.md) method for details. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [`NSControl.TextDidBeginEditingMessage`](./textdidbegineditingmessage.md).

## See Also

### Control-Editing Notifications
- [class let textDidChangeNotification: NSNotification.Name](./textdidchangenotification.md)
  Sent when the text in the receiving control changes.
- [class let textDidEndEditingNotification: NSNotification.Name](./textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/textdidbegineditingnotification)*