# fullScreenAccessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The toolbar’s full screen accessory view.

**Availability**:
- macOS 10.7+ - Deprecated in 10.13

> **Deprecated**: Use an [`NSTitlebarAccessoryViewController`](../nstitlebaraccessoryviewcontroller.md) with an [`NSWindow`](../nswindow.md) instead.

## Declaration

```swift
var fullScreenAccessoryView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * fullScreenAccessoryView;
```

## Discussion

When entering full screen mode, the accessory view is removed from the window if necessary, and attaches underneath the toolbar.

When leaving full screen mode, the accessory view is returned to the window, if it was in the window previously.

To customize this behavior, you can implement the [`NSWindow`](../nswindow.md) delegate method [`windowWillExitFullScreen(_:)`](../nswindowdelegate/windowwillexitfullscreen%28_%29.md).

## See Also

### Deprecated properties
- [var showsBaselineSeparator: Bool](./showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var configuration: [String : Any]](./configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [var centeredItemIdentifier: NSToolbarItem.Identifier?](./centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryViewMinHeight: CGFloat](./fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](./fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [var sizeMode: NSToolbar.SizeMode](./sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryview)*