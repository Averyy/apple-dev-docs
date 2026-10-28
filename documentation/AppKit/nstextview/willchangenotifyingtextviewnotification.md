# willChangeNotifyingTextViewNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when a new text view is established as the text view that sends notifications.

**Availability**:
- macOS

## Declaration

```swift
class let willChangeNotifyingTextViewNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextViewWillChangeNotifyingTextViewNotification;
```

## Discussion

This notification allows observers to reregister themselves for the new text view. Methods such as [`removeTextContainer(at:)`](../nslayoutmanager/removetextcontainer%28at%29.md), [`textContainerChangedTextView(_:)`](../nslayoutmanager/textcontainerchangedtextview%28_%29.md), and [`insertTextContainer(_:at:)`](../nslayoutmanager/inserttextcontainer%28_,at%29.md) cause this notification to be posted.

The notification object is the old notifying text view, or `nil`. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldNotifyingTextView"` | The old `NSTextView`, if one exists, otherwise `nil`. |
| `@"NSNewNotifyingTextView"` | The new `NSTextView`, if one exists, otherwise `nil`. |

There’s no delegate method associated with this notification. The text-handling system ensures that when a new text view replaces an old one as the notifying text view, the existing delegate becomes the delegate of the new text view, and the delegate is registered to receive text view notifications from the new notifying text view. All other observers are responsible for registering themselves on receiving this notification.

## See Also

### Related Documentation
- [func removeObserver(Any)](../../Foundation/notificationcenter/removeobserver%28_%29-2yciv.md)
  Removes all entries specifying an observer from the notification center’s dispatch table.
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: Any?)](../../Foundation/notificationcenter/addobserver%28_,selector,name,object%29.md)
  Adds an entry to the notification center to call the provided selector with the notification.
### Notifications
- [class let didChangeSelectionNotification: NSNotification.Name](./didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](./didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](./didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](./willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/willchangenotifyingtextviewnotification)*