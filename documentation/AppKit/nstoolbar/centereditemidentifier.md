# centeredItemIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The item to display in the center of the toolbar.

**Availability**:
- macOS 10.14+ - Deprecated in 27.0

> **Deprecated**: Use [`centeredItemIdentifiers`](./centereditemidentifiers.md) instead.

## Declaration

```swift
var centeredItemIdentifier: NSToolbarItem.Identifier? { get set }
```

```objc
@property (copy, nullable) NSToolbarItemIdentifier centeredItemIdentifier;
```

## See Also

### Deprecated properties
- [var showsBaselineSeparator: Bool](./showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
- [var configuration: [String : Any]](./configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [var fullScreenAccessoryView: NSView?](./fullscreenaccessoryview.md)
  The toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMinHeight: CGFloat](./fullscreenaccessoryviewminheight.md)
  The minimum height of the toolbar’s full screen accessory view.
- [var fullScreenAccessoryViewMaxHeight: CGFloat](./fullscreenaccessoryviewmaxheight.md)
  The maximum height of the toolbar’s full screen accessory view, in points.
- [var sizeMode: NSToolbar.SizeMode](./sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/centereditemidentifier)*