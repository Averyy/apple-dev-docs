# frame

**Framework**: AppKit  
**Kind**: property

The layout guide’s frame in its owning view’s coordinate system.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var frame: NSRect { get }
```

#### Discussion

The layout guide defines a rectangular space in its owning view’s coordinate system. This property contains a valid [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) value by the time its owning view’s [`layout()`](nsview/layout().md) method is called.

## See Also

- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [var identifier: NSUserInterfaceItemIdentifier](nslayoutguide/identifier.md)
  A string used to identify the layout guide.
- [var owningView: NSView?](nslayoutguide/owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/frame)*