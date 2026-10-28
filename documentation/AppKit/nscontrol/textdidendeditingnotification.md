# textDidEndEditingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent when a control with editable cells ends an editing session.

**Availability**:
- macOS

## Declaration

```swift
class let textDidEndEditingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSControlTextDidEndEditingNotification;
```

## Discussion

The field editor of the edited cell originally sends an [`textDidEndEditingNotification`](./textdidendeditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [`controlTextDidEndEditing:`](../../ObjectiveC/nsobject-swift.class/controltextdidendediting_.md) method for details. The system posts this notification on the main actor.

To observe this notification using Swift concurrency, use [`NSControl.TextDidEndEditingMessage`](./textdidendeditingmessage.md).

## See Also

### Control-Editing Notifications
- [class let textDidBeginEditingNotification: NSNotification.Name](./textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidChangeNotification: NSNotification.Name](./textdidchangenotification.md)
  Sent when the text in the receiving control changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/textdidendeditingnotification)*