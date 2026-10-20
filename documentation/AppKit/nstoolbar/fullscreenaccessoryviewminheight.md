# fullScreenAccessoryViewMinHeight

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum height of the toolbar’s full screen accessory view.

**Availability**:
- macOS 10.7+ - Deprecated in 10.13

> **Deprecated**: Use an [`NSTitlebarAccessoryViewController`](../nstitlebaraccessoryviewcontroller.md) and its [`fullScreenMinHeight`](../nstitlebaraccessoryviewcontroller/fullscreenminheight.md) property with an [`NSWindow`](../nswindow.md) instead.

## Declaration

```swift
var fullScreenAccessoryViewMinHeight: CGFloat { get set }
```

```objc
@property CGFloat fullScreenAccessoryViewMinHeight;
```

#### Discussion

The [`fullScreenAccessoryViewMinHeight`](./fullscreenaccessoryviewminheight.md) is used when the menu bar is hidden. During the reveal, the toolbar’s accessory view’s frame is interpolated between its [`fullScreenAccessoryViewMinHeight`](./fullscreenaccessoryviewminheight.md) and [`fullScreenAccessoryViewMaxHeight`](./fullscreenaccessoryviewmaxheight.md).

If the minimum height is 0 the accessory view isn’t resized; instead a special transition is used to reveal it with the menu bar. This simplifies the accessory view’s task, because it doesn’t have to handle the case of the height being set to `0`.

To create a fixed-height accessory view, set the [`fullScreenAccessoryViewMaxHeight`](./fullscreenaccessoryviewmaxheight.md) and [`fullScreenAccessoryViewMinHeight`](./fullscreenaccessoryviewminheight.md) properties to be equal.

The default value is 0.

## See Also

### Deprecated properties
- [var showsBaselineSeparator: Bool](./showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var configuration: [String : Any]](./configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [var centeredItemIdentifier: NSToolbarItem.Identifier?](./centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](./fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](./fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [var sizeMode: NSToolbar.SizeMode](./sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryviewminheight)*