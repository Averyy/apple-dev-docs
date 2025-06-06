# textDidBeginEditingNotification

**Framework**: AppKit  
**Kind**: property

Sent when a control with editable cells begins an edit session.

**Availability**:
- macOS ?+

## Declaration

```swift
class let textDidBeginEditingNotification: NSNotification.Name
```

#### Discussion

The field editor of the edited cell originally sends an [`didBeginEditingNotification`](nstext/didbegineditingnotification.md) to the control, which passes it on in this form to its delegate. The notification object is the `NSControl` object posting the notification. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `“NSFieldEditor”` | The edited cell’s field editor |

See the [`controlTextDidEndEditing:`](https://developer.apple.com/documentation/objectivec/nsobject/1428847-controltextdidendediting) method for details. The system posts this notification on the main actor.

## See Also

- [class let textDidChangeNotification: NSNotification.Name](nscontrol/textdidchangenotification.md)
  Sent when the text in the receiving control changes.
- [class let textDidEndEditingNotification: NSNotification.Name](nscontrol/textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/textdidbegineditingnotification)*