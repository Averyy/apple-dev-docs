# didChangeItemNotification

**Framework**: AppKit  
**Kind**: property

Posted after a menu item in the menu changes appearance.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didChangeItemNotification: NSNotification.Name
```

#### Discussion

Changes include enabling/disabling, changes in state, and changes to title. The notification object is the instance of `NSMenu` with the menu item that changed. The `userInfo` dictionary contains the following information.

| Key | Value |
| --- | --- |
| `@"NSMenuItemIndex"` | An `NSNumber` object containing the integer index of the menu item that changed. |

## See Also

- [class let didAddItemNotification: NSNotification.Name](nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didBeginTrackingNotification: NSNotification.Name](nsmenu/didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didEndTrackingNotification: NSNotification.Name](nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](nsmenu/didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/didchangeitemnotification)*