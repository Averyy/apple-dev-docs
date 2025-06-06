# owningView

**Framework**: AppKit  
**Kind**: property

The view that owns this layout guide.

**Availability**:
- macOS 10.11+

## Declaration

```swift
weak var owningView: NSView? { get set }
```

#### Discussion

By default, this property is `nil`.  To participate in Auto Layout, the layout guide must be added to a view by calling its [`addLayoutGuide(_:)`](nsview/addlayoutguide(_:).md) method. Do not modify this property directly. Instead, use the view’s [`addLayoutGuide(_:)`](nsview/addlayoutguide(_:).md) and [`removeLayoutGuide(_:)`](nsview/removelayoutguide(_:).md) methods, which update this property as necessary.

## See Also

- [var identifier: NSUserInterfaceItemIdentifier](nslayoutguide/identifier.md)
  A string used to identify the layout guide.
- [var frame: NSRect](nslayoutguide/frame.md)
  The layout guide’s frame in its owning view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/owningview)*