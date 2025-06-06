# didSendActionNotification

**Framework**: AppKit  
**Kind**: property

Posted just after the application dispatches a menu item’s action method to the menu item’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didSendActionNotification: NSNotification.Name
```

#### Discussion

The notification object is the instance of `NSMenu` containing the chosen menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
| --- | --- |
| `@"MenuItem"` | The menu item that was chosen. |

## See Also

- [class let didAddItemNotification: NSNotification.Name](nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didChangeItemNotification: NSNotification.Name](nsmenu/didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didBeginTrackingNotification: NSNotification.Name](nsmenu/didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didEndTrackingNotification: NSNotification.Name](nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let willSendActionNotification: NSNotification.Name](nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/didsendactionnotification)*