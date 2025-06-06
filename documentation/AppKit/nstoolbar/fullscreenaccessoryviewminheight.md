# fullScreenAccessoryViewMinHeight

**Framework**: AppKit  
**Kind**: property

The minimum height of the toolbar’s full screen accessory view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var fullScreenAccessoryViewMinHeight: CGFloat { get set }
```

#### Discussion

The [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) is used when the menu bar is hidden. During the reveal, the toolbar’s accessory view’s frame is interpolated between its [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) and [`fullScreenAccessoryViewMaxHeight`](nstoolbar/fullscreenaccessoryviewmaxheight.md).

If the minimum height is 0 the accessory view isn’t resized; instead a special transition is used to reveal it with the menu bar. This simplifies the accessory view’s task, because it doesn’t have to handle the case of the height being set to `0`.

To create a fixed-height accessory view, set the [`fullScreenAccessoryViewMaxHeight`](nstoolbar/fullscreenaccessoryviewmaxheight.md) and [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) properties to be equal.

The default value is 0.

## See Also

- [var centeredItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](nstoolbar/fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](nstoolbar/fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [var sizeMode: NSToolbar.SizeMode](nstoolbar/sizemode-swift.property.md)
  The toolbar’s size mode.
- [NSToolbar.SizeMode](nstoolbar/sizemode-swift.enum.md)
  Constants that specify toolbar display modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryviewminheight)*