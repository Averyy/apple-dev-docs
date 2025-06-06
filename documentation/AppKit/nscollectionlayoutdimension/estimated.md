# estimated(_:)

**Framework**: AppKit  
**Kind**: method

Creates a dimension with an estimated point value.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class func estimated(_ estimatedDimension: CGFloat) -> Self
```

#### Discussion

The final size of the dimension is determined when the content is rendered.

## See Also

- [class func absolute(CGFloat) -> Self](nscollectionlayoutdimension/absolute(_:).md)
  Creates a dimension with an absolute point value.
- [class func fractionalHeight(CGFloat) -> Self](nscollectionlayoutdimension/fractionalheight(_:).md)
  Creates a dimension that is computed as a fraction of the height of the containing group.
- [class func fractionalWidth(CGFloat) -> Self](nscollectionlayoutdimension/fractionalwidth(_:).md)
  Creates a dimension that is computed as a fraction of the width of the containing group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutdimension/estimated(_:))*