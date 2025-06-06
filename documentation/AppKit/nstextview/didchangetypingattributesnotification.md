# didChangeTypingAttributesNotification

**Framework**: AppKit  
**Kind**: property

Posted when there is a change in the typing attributes within a text view.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didChangeTypingAttributesNotification: NSNotification.Name
```

#### Discussion

This notification is posted, via the [`textViewDidChangeTypingAttributes(_:)`](nstextviewdelegate/textviewdidchangetypingattributes(_:).md) delegate method, whether or not text has changed as a result of the attribute change.

## See Also

- [class let didChangeSelectionNotification: NSNotification.Name](nstextview/didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](nstextview/willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/didchangetypingattributesnotification)*