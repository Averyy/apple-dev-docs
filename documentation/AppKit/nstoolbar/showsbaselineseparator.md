# showsBaselineSeparator

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var showsBaselineSeparator: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar shows the separator between the toolbar and the main window contents. If the value is [`false`](https://developer.apple.com/documentation/swift/false), the toolbar doesn’t show the separator. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

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
- [var sizeMode: NSToolbar.SizeMode](nstoolbar/sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/showsbaselineseparator)*