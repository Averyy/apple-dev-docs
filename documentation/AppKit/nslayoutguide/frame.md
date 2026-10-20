# frame

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout guide’s frame in its owning view’s coordinate system.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var frame: NSRect { get }
```

```objc
@property (readonly) NSRect frame;
```

#### Discussion

The layout guide defines a rectangular space in its owning view’s coordinate system. This property contains a valid [`CGRect`](../../CoreFoundation/cgrect.md) value by the time its owning view’s [`layout()`](../nsview/layout%28%29.md) method is called.

## See Also

### Related Documentation
- [func layout()](../nsview/layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
### Working With Layout Guides
- [var identifier: NSUserInterfaceItemIdentifier](./identifier.md)
  A string used to identify the layout guide.
- [var owningView: NSView?](./owningview.md)
  The view that owns this layout guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutguide/frame)*