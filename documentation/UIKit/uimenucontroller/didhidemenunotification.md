# didHideMenuNotification

**Framework**: UIKit  
**Kind**: property

Posted by the menu controller just after it hides the menu.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let didHideMenuNotification: NSNotification.Name
```

#### Discussion

There is no `userInfo` dictionary.

## See Also

- [class let willShowMenuNotification: NSNotification.Name](uimenucontroller/willshowmenunotification.md)
  Posted by the menu controller just before it shows the menu.
- [class let didShowMenuNotification: NSNotification.Name](uimenucontroller/didshowmenunotification.md)
  Posted by the menu controller just after it shows the menu.
- [class let willHideMenuNotification: NSNotification.Name](uimenucontroller/willhidemenunotification.md)
  Posted by the menu controller just before it hides the menu.
- [class let menuFrameDidChangeNotification: NSNotification.Name](uimenucontroller/menuframedidchangenotification.md)
  Posted when the frame of a visible menu changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/didhidemenunotification)*