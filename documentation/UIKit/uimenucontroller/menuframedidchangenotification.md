# menuFrameDidChangeNotification

**Framework**: UIKit  
**Kind**: property

Posted when the frame of a visible menu changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let menuFrameDidChangeNotification: NSNotification.Name
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
- [class let didHideMenuNotification: NSNotification.Name](uimenucontroller/didhidemenunotification.md)
  Posted by the menu controller just after it hides the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/menuframedidchangenotification)*