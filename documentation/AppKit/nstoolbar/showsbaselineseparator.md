# showsBaselineSeparator

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: No longer supported

## Declaration

```swift
var showsBaselineSeparator: Bool { get set }
```

```objc
@property BOOL showsBaselineSeparator;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), the toolbar shows the separator between the toolbar and the main window contents. If the value is [`false`](../../Swift/false.md), the toolbar doesn’t show the separator. The default value is [`false`](../../Swift/false.md).

## See Also

### Deprecated properties
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
- [var sizeMode: NSToolbar.SizeMode](./sizemode-swift.property.md)
  The toolbar’s size mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/showsbaselineseparator)*