# willHideMenuNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Posted by the menu controller just before it hides the menu.

**Availability**:
- iOS 3.0+ - Deprecated in 16.0
- iPadOS 3.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`UIEditMenuInteraction`](../uieditmenuinteraction.md) instead.

## Declaration

```swift
nonisolated
class let willHideMenuNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIMenuControllerWillHideMenuNotification;
```

## Discussion

There is no `userInfo` dictionary.

## See Also

### Notifications
- [class let willShowMenuNotification: NSNotification.Name](./willshowmenunotification.md)
  Posted by the menu controller just before it shows the menu.
- [class let didShowMenuNotification: NSNotification.Name](./didshowmenunotification.md)
  Posted by the menu controller just after it shows the menu.
- [class let didHideMenuNotification: NSNotification.Name](./didhidemenunotification.md)
  Posted by the menu controller just after it hides the menu.
- [class let menuFrameDidChangeNotification: NSNotification.Name](./menuframedidchangenotification.md)
  Posted when the frame of a visible menu changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/willhidemenunotification)*