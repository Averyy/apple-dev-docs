# didBeginTrackingNotification

**Framework**: AppKit  
**Kind**: property

Posted when menu tracking begins.

**Availability**:
- macOS ?+

## Declaration

```swift
class let didBeginTrackingNotification: NSNotification.Name
```

#### Discussion

The notification object is the main menu bar (`[NSApp mainMenu]`) or the root menu of a popup button. This notification does not contain a `userInfo` dictionary.

> **Note**:  This notification is available in versions 10.3 and 10.4 of macOS, however it is not publicly declared so you must declare the name constant as an `extern`, for example: ```objc
extern NSString *NSMenuDidBeginTrackingNotification;
```

 This notification is available in versions 10.3 and 10.4 of macOS, however it is not publicly declared so you must declare the name constant as an `extern`, for example:

```objc
extern NSString *NSMenuDidBeginTrackingNotification;
```

## See Also

- [class let didAddItemNotification: NSNotification.Name](nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didChangeItemNotification: NSNotification.Name](nsmenu/didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didEndTrackingNotification: NSNotification.Name](nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](nsmenu/didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/didbegintrackingnotification)*