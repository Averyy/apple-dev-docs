# didChangeTypingAttributesNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when there is a change in the typing attributes within a text view.

**Availability**:
- macOS

## Declaration

```swift
class let didChangeTypingAttributesNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextViewDidChangeTypingAttributesNotification;
```

#### Discussion

This notification is posted, via the [`textViewDidChangeTypingAttributes(_:)`](../nstextviewdelegate/textviewdidchangetypingattributes%28_%29.md) delegate method, whether or not text has changed as a result of the attribute change.

To observe this notification using Swift concurrency, use [`NSTextView.DidChangeTypingAttributesMessage`](./didchangetypingattributesmessage.md).

## See Also

### Notifications
- [class let didChangeSelectionNotification: NSNotification.Name](./didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](./willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](./didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](./willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/didchangetypingattributesnotification)*