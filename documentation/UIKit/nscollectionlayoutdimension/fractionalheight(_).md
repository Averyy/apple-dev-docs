# fractionalHeight(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a dimension that is computed as a fraction of the height of the containing group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func fractionalHeight(_ fractionalHeight: CGFloat) -> Self
```

```objc
+ (instancetype) fractionalHeightDimension:(CGFloat) fractionalHeight;
```

## See Also

### Creating a dimension
- [class func absolute(CGFloat) -> Self](./absolute%28_%29.md)
  Creates a dimension with an absolute point value.
- [class func estimated(CGFloat) -> Self](./estimated%28_%29.md)
  Creates a dimension with an estimated point value.
- [class func fractionalWidth(CGFloat) -> Self](./fractionalwidth%28_%29.md)
  Creates a dimension that is computed as a fraction of the width of the containing group.
- [class func uniformAcrossSiblings(estimate: CGFloat) -> Self](./uniformacrosssiblings%28estimate%29.md)
  Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension/fractionalheight(_:))*