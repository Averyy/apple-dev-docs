# willChangeNotifyingTextViewNotification

**Framework**: AppKit  
**Kind**: property

Posted when a new text view is established as the text view that sends notifications.

**Availability**:
- macOS ?+

## Declaration

```swift
class let willChangeNotifyingTextViewNotification: NSNotification.Name
```

#### Discussion

This notification allows observers to reregister themselves for the new text view. Methods such as [`removeTextContainer(at:)`](nslayoutmanager/removetextcontainer(at:).md), [`textContainerChangedTextView(_:)`](nslayoutmanager/textcontainerchangedtextview(_:).md), and [`insertTextContainer(_:at:)`](nslayoutmanager/inserttextcontainer(_:at:).md) cause this notification to be posted.

The notification object is the old notifying text view, or `nil`. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSOldNotifyingTextView"` | The old `NSTextView`, if one exists, otherwise `nil`. |
| `@"NSNewNotifyingTextView"` | The new `NSTextView`, if one exists, otherwise `nil`. |

There’s no delegate method associated with this notification. The text-handling system ensures that when a new text view replaces an old one as the notifying text view, the existing delegate becomes the delegate of the new text view, and the delegate is registered to receive text view notifications from the new notifying text view. All other observers are responsible for registering themselves on receiving this notification.

## See Also

- [func removeObserver(Any)](../Foundation/NotificationCenter/removeObserver(_:)-2yciv.md)
  Removes all entries specifying an observer from the notification center’s dispatch table.
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: Any?)](../Foundation/NotificationCenter/addObserver(_:selector:name:object:).md)
  Adds an entry to the notification center to call the provided selector with the notification.
- [class let didChangeSelectionNotification: NSNotification.Name](nstextview/didchangeselectionnotification.md)
  Posted when the selected range of characters changes.
- [class let didChangeTypingAttributesNotification: NSNotification.Name](nstextview/didchangetypingattributesnotification.md)
  Posted when there is a change in the typing attributes within a text view.
- [class let didSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/didswitchtonslayoutmanagernotification.md)
  Posted by the framework after switching to using the compatibility mode layout manager.
- [class let willSwitchToNSLayoutManagerNotification: NSNotification.Name](nstextview/willswitchtonslayoutmanagernotification.md)
  Posted by the framework before switching to the compatibility mode layout manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/willchangenotifyingtextviewnotification)*