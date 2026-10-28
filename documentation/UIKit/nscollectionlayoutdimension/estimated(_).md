# estimated(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a dimension with an estimated point value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func estimated(_ estimatedDimension: CGFloat) -> Self
```

```objc
+ (instancetype) estimatedDimension:(CGFloat) estimatedDimension;
```

## Discussion

The final size of the dimension is determined when the content is rendered.

## See Also

### Creating a dimension
- [class func absolute(CGFloat) -> Self](./absolute%28_%29.md)
  Creates a dimension with an absolute point value.
- [class func fractionalHeight(CGFloat) -> Self](./fractionalheight%28_%29.md)
  Creates a dimension that is computed as a fraction of the height of the containing group.
- [class func fractionalWidth(CGFloat) -> Self](./fractionalwidth%28_%29.md)
  Creates a dimension that is computed as a fraction of the width of the containing group.
- [class func uniformAcrossSiblings(estimate: CGFloat) -> Self](./uniformacrosssiblings%28estimate%29.md)
  Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension/estimated(_:))*