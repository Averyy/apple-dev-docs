# configuration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A dictionary containing the current configuration details for the toolbar.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: Use -itemIdentifiers and -displayMode instead.

## Declaration

```swift
var configuration: [String : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * configurationDictionary;
```

## Discussion

Use this property to retrieve the toolbar’s configuration details so you can save them to disk yourself. The dictionary in this property contains the identifiers of the current toolbar items and the values of important properties such as [`displayMode`](./displaymode-swift.property.md) and [`isVisible`](./isvisible.md).

## See Also

### Deprecated properties
- [var showsBaselineSeparator: Bool](./showsbaselineseparator.md)
  A Boolean value that indicates whether the toolbar shows the separator between the toolbar and the main window contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/configuration)*