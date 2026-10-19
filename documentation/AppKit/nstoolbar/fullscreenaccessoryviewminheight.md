# fullScreenAccessoryViewMinHeight

**Framework**: AppKit  
**Kind**: property

The minimum height of the toolbar’s full screen accessory view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var fullScreenAccessoryViewMinHeight: CGFloat { get set }
```

#### Discussion

The [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) is used when the menu bar is hidden. During the reveal, the toolbar’s accessory view’s frame is interpolated between its [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) and [`fullScreenAccessoryViewMaxHeight`](nstoolbar/fullscreenaccessoryviewmaxheight.md).

If the minimum height is 0 the accessory view isn’t resized; instead a special transition is used to reveal it with the menu bar. This simplifies the accessory view’s task, because it doesn’t have to handle the case of the height being set to `0`.

To create a fixed-height accessory view, set the [`fullScreenAccessoryViewMaxHeight`](nstoolbar/fullscreenaccessoryviewmaxheight.md) and [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) properties to be equal.

The default value is 0.

## See Also

- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var configuration: [String : Any]](nstoolbar/configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [var centeredItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](nstoolbar/fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](nstoolbar/fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [var sizeMode: NSToolbar.SizeMode](nstoolbar/sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryviewminheight)*