# frame

**Framework**: AppKit  
**Kind**: property

The frame rectangle of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var frame: NSRect { get set }
```

#### Discussion

The frame rectangle is measured in points and specified in the collection view’s coordinate system. Setting the value of this property also updates the value in the [`size`](nscollectionviewlayoutattributes/size.md) property.

## See Also

- [var size: NSSize](nscollectionviewlayoutattributes/size.md)
  The size of the element.
- [var alpha: CGFloat](nscollectionviewlayoutattributes/alpha.md)
  The transparency of the element.
- [var isHidden: Bool](nscollectionviewlayoutattributes/ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](nscollectionviewlayoutattributes/zindex.md)
  The element’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/frame)*