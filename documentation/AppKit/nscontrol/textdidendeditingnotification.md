# textDidEndEditingNotification

**Framework**: AppKit  
**Kind**: property

Sent when a control with editable cells ends an editing session.

**Availability**:
- macOS ?+

## Declaration

```swift
class let textDidEndEditingNotification: NSNotification.Name
```

#### Discussion

The field editor of the edited cell originally sends an [`textDidEndEditingNotification`](nscontrol/textdidendeditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [`controlTextDidEndEditing:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/controlTextDidEndEditing:) method for details. The system posts this notification on the main actor.

## See Also

- [class let textDidBeginEditingNotification: NSNotification.Name](nscontrol/textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidChangeNotification: NSNotification.Name](nscontrol/textdidchangenotification.md)
  Sent when the text in the receiving control changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/textdidendeditingnotification)*