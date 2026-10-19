# sizeMode

**Framework**: AppKit  
**Kind**: property

The toolbar’s size mode.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var sizeMode: NSToolbar.SizeMode { get set }
```

#### Discussion

If there’s no icon of the given size for a toolbar item, the toolbar item creates one by scaling an icon of another size.

## See Also

- [var showsBaselineSeparator: Bool](nstoolbar/showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var configuration: [String : Any]](nstoolbar/configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [var centeredItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/centereditemidentifier.md)
  The item to display in the center of the toolbar.
- [var fullScreenAccessoryView: NSView?](nstoolbar/fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMinHeight: CGFloat](nstoolbar/fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](nstoolbar/fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/sizemode-swift.property)*