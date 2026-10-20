# sizeMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The toolbar’s size mode.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: The toolbar ignores this property.

## Declaration

```swift
var sizeMode: NSToolbar.SizeMode { get set }
```

```objc
@property NSToolbarSizeMode sizeMode;
```

#### Discussion

If there’s no icon of the given size for a toolbar item, the toolbar item creates one by scaling an icon of another size.

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
- [var fullScreenAccessoryViewMaxHeight: CGFloat](./fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/sizemode-swift.property)*