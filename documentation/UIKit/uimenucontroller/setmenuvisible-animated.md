# setMenuVisible(_:animated:)

**Framework**: UIKit  
**Kind**: method

Shows or hides the editing menu, optionally animating the action.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setMenuVisible(_ menuVisible: Bool, animated: Bool)
```

#### Discussion

Before showing the menu, be sure to position it relative to the selection. See [`setTargetRect(_:in:)`](uimenucontroller/settargetrect(_:in:).md) for details. If you do not set the target rect before displaying the menu, it appears at screen coordinates (0.0, 0.0).

## Parameters

- `menuVisible`:   if the menu should be shown,   if it should be hidden.
- `animated`:   if the showing or hiding of the menu should be animated, otherwise  .

## See Also

- [func showMenu(from: UIView, rect: CGRect)](uimenucontroller/showmenu(from:rect:).md)
- [func hideMenu(from: UIView)](uimenucontroller/hidemenu(from:).md)
- [func hideMenu()](uimenucontroller/hidemenu.md)
- [var isMenuVisible: Bool](uimenucontroller/ismenuvisible.md)
  The visibility of the editing menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/setmenuvisible(_:animated:))*