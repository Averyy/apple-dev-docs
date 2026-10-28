# didAddItemNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after a menu item is added to the menu.

**Availability**:
- macOS

## Declaration

```swift
class let didAddItemNotification: NSNotification.Name
```

```c
extern NSNotificationName NSMenuDidAddItemNotification;
```

## Discussion

The notification object is the instance of `NSMenu` that just added the new menu item. The `userInfo` dictionary contains the following information.

| Key | Value |
| --- | --- |
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that was added. |

To observe this notification using Swift concurrency, use [`NSMenu.DidAddItemMessage`](./didadditemmessage.md).

## See Also

### Notifications
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
- [class let willSendActionNotification: NSNotification.Name](./willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/didadditemnotification)*