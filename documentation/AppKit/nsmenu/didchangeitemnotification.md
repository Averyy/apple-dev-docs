# didChangeItemNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after a menu item in the menu changes appearance.

**Availability**:
- macOS

## Declaration

```swift
class let didChangeItemNotification: NSNotification.Name
```

```c
extern NSNotificationName NSMenuDidChangeItemNotification;
```

#### Discussion

Changes include enabling/disabling, changes in state, and changes to title. The notification object is the instance of `NSMenu` with the menu item that changed. The `userInfo` dictionary contains the following information.

| Key | Value |
| --- | --- |
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that changed. |

To observe this notification using Swift concurrency, use [`NSMenu.DidChangeItemMessage`](./didchangeitemmessage.md).

## See Also

### Notifications
- [class let didAddItemNotification: NSNotification.Name](./didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didBeginTrackingNotification: NSNotification.Name](./didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didEndTrackingNotification: NSNotification.Name](./didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](./didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](./didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](./willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/didchangeitemnotification)*