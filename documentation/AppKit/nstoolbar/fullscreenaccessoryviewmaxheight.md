# fullScreenAccessoryViewMaxHeight

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum height of the toolbar’s full screen accessory view, in points.

**Availability**:
- macOS 10.7+ - Deprecated in 10.13

> **Deprecated**: Use an [`NSTitlebarAccessoryViewController`](../nstitlebaraccessoryviewcontroller.md) with an [`NSWindow`](../nswindow.md) instead.

## Declaration

```swift
var fullScreenAccessoryViewMaxHeight: CGFloat { get set }
```

```objc
@property CGFloat fullScreenAccessoryViewMaxHeight;
```

#### Discussion

The [`fullScreenAccessoryViewMaxHeight`](./fullscreenaccessoryviewmaxheight.md) is used when displaying a fully revealed menu bar. During the reveal, the toolbar’s accessory view’s frame is interpolated between its [`fullScreenAccessoryViewMinHeight`](./fullscreenaccessoryviewminheight.md) and `fullScreenAccessoryViewMaxHeight` properties.

By default the maximum height gets set to the height of the accessory view’s frame when it’s set.

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
- [var fullScreenAccessoryViewMinHeight: CGFloat](./fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var sizeMode: NSToolbar.SizeMode](./sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryviewmaxheight)*