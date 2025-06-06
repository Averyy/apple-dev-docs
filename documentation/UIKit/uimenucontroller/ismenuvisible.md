# isMenuVisible

**Framework**: UIKit  
**Kind**: property

The visibility of the editing menu.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isMenuVisible: Bool { get set }
```

#### Discussion

Setting this property displays or hides the menu immediately, without animation. For animating the showing or hiding of the menu, use the [`setMenuVisible(_:animated:)`](uimenucontroller/setmenuvisible(_:animated:).md) method. Before showing the menu, be sure to position it relative to the selection.

## See Also

- [func showMenu(from: UIView, rect: CGRect)](uimenucontroller/showmenu(from:rect:).md)
- [func hideMenu(from: UIView)](uimenucontroller/hidemenu(from:).md)
- [func hideMenu()](uimenucontroller/hidemenu.md)
- [func setMenuVisible(Bool, animated: Bool)](uimenucontroller/setmenuvisible(_:animated:).md)
  Shows or hides the editing menu, optionally animating the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/ismenuvisible)*