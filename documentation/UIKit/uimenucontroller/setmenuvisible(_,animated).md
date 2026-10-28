# setMenuVisible(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Shows or hides the editing menu, optionally animating the action.

**Availability**:
- iOS 3.0+ - Deprecated in 13.0
- iPadOS 3.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIMenuController`](../uimenucontroller.md).

## Declaration

```swift
func setMenuVisible(_ menuVisible: Bool, animated: Bool)
```

```objc
- (void) setMenuVisible:(BOOL) menuVisible animated:(BOOL) animated;
```

## Discussion

Before showing the menu, be sure to position it relative to the selection. See [`setTargetRect(_:in:)`](./settargetrect%28_,in%29.md) for details. If you do not set the target rect before displaying the menu, it appears at screen coordinates (0.0, 0.0).

## Parameters

- `menuVisible`: [`true`](../../Swift/true.md) if the menu should be shown, [`false`](../../Swift/false.md) if it should be hidden.
- `animated`: [`true`](../../Swift/true.md) if the showing or hiding of the menu should be animated, otherwise [`false`](../../Swift/false.md).

## See Also

### Showing and hiding the menu
- [func showMenu(from: UIView, rect: CGRect)](./showmenu%28from,rect%29.md)
- [func hideMenu(from: UIView)](./hidemenu%28from%29.md)
- [func hideMenu()](./hidemenu%28%29.md)
- [var isMenuVisible: Bool](./ismenuvisible.md)
  The visibility of the editing menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/setmenuvisible(_:animated:))*