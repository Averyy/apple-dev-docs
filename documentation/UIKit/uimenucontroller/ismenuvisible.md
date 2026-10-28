# isMenuVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visibility of the editing menu.

**Availability**:
- iOS 3.0+ - Deprecated in 16.0
- iPadOS 3.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIMenuController`](../uimenucontroller.md).

## Declaration

```swift
var isMenuVisible: Bool { get set }
```

```objc
@property (nonatomic, getter=isMenuVisible) BOOL menuVisible;
```

## Discussion

Setting this property displays or hides the menu immediately, without animation. For animating the showing or hiding of the menu, use the [`setMenuVisible(_:animated:)`](./setmenuvisible%28_,animated%29.md) method. Before showing the menu, be sure to position it relative to the selection.

## See Also

### Showing and hiding the menu
- [func showMenu(from: UIView, rect: CGRect)](./showmenu%28from,rect%29.md)
- [func hideMenu(from: UIView)](./hidemenu%28from%29.md)
- [func hideMenu()](./hidemenu%28%29.md)
- [func setMenuVisible(Bool, animated: Bool)](./setmenuvisible%28_,animated%29.md)
  Shows or hides the editing menu, optionally animating the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenucontroller/ismenuvisible)*