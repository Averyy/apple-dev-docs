# didChangeSelectionNotification

**Framework**: AppKit  
**Kind**: property

Posted when the selected range of characters changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didChangeSelectionNotification: NSNotification.Name
```

#### Discussion

`NSTextView` posts this notification whenever [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md) is invoked, either directly or through the many methods ([`mouseDown(with:)`](nsresponder/mousedown(with:).md), [`selectAll(_:)`](nstext/selectall(_:).md), and so on) that invoke it indirectly. When the user is selecting text, this notification is posted only once, at the end of the selection operation. The text view’s delegate receives a [`textViewDidChangeSelection(_:)`](nstextviewdelegate/textviewdidchangeselection(_:).md) message when this notification is posted.

The notification object is the notifying text view. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldSelectedCharacterRange"` | An `NSValue` object containing an `NSRange` structure with the originally selected range. |

## See Also

- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](nstextview/willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](nstextview/didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/didchangeselectionnotification)*