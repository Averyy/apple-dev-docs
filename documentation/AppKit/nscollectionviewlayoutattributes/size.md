# size

**Framework**: AppKit  
**Kind**: property

The size of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var size: NSSize { get set }
```

#### Discussion

Setting the value of this property also updates the value in the [`frame`](nscollectionviewlayoutattributes/frame.md) property.

## See Also

- [var frame: NSRect](nscollectionviewlayoutattributes/frame.md)
  The frame rectangle of the element.
- [var alpha: CGFloat](nscollectionviewlayoutattributes/alpha.md)
  The transparency of the element.
- [var isHidden: Bool](nscollectionviewlayoutattributes/ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](nscollectionviewlayoutattributes/zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/size)*