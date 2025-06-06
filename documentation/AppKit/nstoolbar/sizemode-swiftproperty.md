# sizeMode

**Framework**: AppKit  
**Kind**: property

The toolbar’s size mode.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var sizeMode: NSToolbar.SizeMode { get set }
```

#### Discussion

If there’s no icon of the given size for a toolbar item, the toolbar item creates one by scaling an icon of another size.

## See Also

- [var centeredItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](nstoolbar/fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMinHeight: CGFloat](nstoolbar/fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](nstoolbar/fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [NSToolbar.SizeMode](nstoolbar/sizemode-swift.enum.md)
  Constants that specify toolbar display modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/sizemode-swift.property)*