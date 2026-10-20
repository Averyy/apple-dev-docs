# willSendActionNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted just before the application dispatches a menu item’s action method to the menu item’s target.

**Availability**:
- macOS

## Declaration

```swift
class let willSendActionNotification: NSNotification.Name
```

```c
extern NSNotificationName NSMenuWillSendActionNotification;
```

#### Discussion

The notification object is the instance of `NSMenu` containing the chosen menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
| --- | --- |
| `@"MenuItem"` | The menu item that was chosen. |

To observe this notification using Swift concurrency, use [`NSMenu.WillSendActionMessage`](./willsendactionmessage.md).

## See Also

### Notifications
- [class let didAddItemNotification: NSNotification.Name](./didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didChangeItemNotification: NSNotification.Name](./didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didBeginTrackingNotification: NSNotification.Name](./didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didEndTrackingNotification: NSNotification.Name](./didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](./didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](./didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/willsendactionnotification)*