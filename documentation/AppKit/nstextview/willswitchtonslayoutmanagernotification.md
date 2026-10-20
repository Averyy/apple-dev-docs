# willSwitchToNSLayoutManagerNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted by the framework before switching to the compatibility mode layout manager.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class let willSwitchToNSLayoutManagerNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextViewWillSwitchToNSLayoutManagerNotification;
```

## See Also

### Notifications
- [class let didChangeSelectionNotification: NSNotification.Name](./didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let willChangeNotifyingTextViewNotification: NSNotification.Name](./willchangenotifyingtextviewnotification.md)
  Posted when a new text view is established as the text view that sends notifications.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](./didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](./didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/willswitchtonslayoutmanagernotification)*