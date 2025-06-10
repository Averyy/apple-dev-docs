# absolute(_:)

**Framework**: UIKit  
**Kind**: method

Creates a dimension with an absolute point value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func absolute(_ absoluteDimension: CGFloat) -> Self
```

## See Also

- [class func estimated(CGFloat) -> Self](nscollectionlayoutdimension/estimated(_:).md)
  Creates a dimension with an estimated point value.
- [class func fractionalHeight(CGFloat) -> Self](nscollectionlayoutdimension/fractionalheight(_:).md)
  Creates a dimension that is computed as a fraction of the height of the containing group.
- [class func fractionalWidth(CGFloat) -> Self](nscollectionlayoutdimension/fractionalwidth(_:).md)
  Creates a dimension that is computed as a fraction of the width of the containing group.
- [class func uniformAcrossSiblings(estimate: CGFloat) -> Self](nscollectionlayoutdimension/uniformacrosssiblings(estimate:).md)
  Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension/absolute(_:))*