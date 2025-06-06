# textDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Sent when the text in the receiving control changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let textDidChangeNotification: NSNotification.Name
```

#### Discussion

The field editor of the edited cell originally sends an [`didChangeNotification`](nstext/didchangenotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [`controlTextDidChange:`](https://developer.apple.com/documentation/objectivec/nsobject/1428982-controltextdidchange) method for details. The system posts this notification on the main actor.

## See Also

- [class let textDidBeginEditingNotification: NSNotification.Name](nscontrol/textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidEndEditingNotification: NSNotification.Name](nscontrol/textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/textdidchangenotification)*