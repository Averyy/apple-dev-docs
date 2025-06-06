# fullScreenAccessoryViewMaxHeight

**Framework**: AppKit  
**Kind**: property

The maximum height of the toolbar’s full screen accessory view, in points.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var fullScreenAccessoryViewMaxHeight: CGFloat { get set }
```

#### Discussion

The [`fullScreenAccessoryViewMaxHeight`](nstoolbar/fullscreenaccessoryviewmaxheight.md) is used when displaying a fully revealed menu bar. During the reveal, the toolbar’s accessory view’s frame is interpolated between its [`fullScreenAccessoryViewMinHeight`](nstoolbar/fullscreenaccessoryviewminheight.md) and `fullScreenAccessoryViewMaxHeight` properties.

By default the maximum height gets set to the height of the accessory view’s frame when it’s set.

## See Also

- [var centeredItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](nstoolbar/fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMinHeight: CGFloat](nstoolbar/fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var sizeMode: NSToolbar.SizeMode](nstoolbar/sizemode-swift.property.md)
  The toolbar’s size mode.
- [NSToolbar.SizeMode](nstoolbar/sizemode-swift.enum.md)
  Constants that specify toolbar display modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/fullscreenaccessoryviewmaxheight)*