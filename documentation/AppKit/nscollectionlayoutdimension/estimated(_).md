# estimated(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a dimension with an estimated point value.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func estimated(_ estimatedDimension: CGFloat) -> Self
```

```objc
+ (instancetype) estimatedDimension:(CGFloat) estimatedDimension;
```

#### Discussion

The final size of the dimension is determined when the content is rendered.

## See Also

### Creating a dimension
- [class func absolute(CGFloat) -> Self](./absolute%28_%29.md)
  Creates a dimension with an absolute point value.
- [class func fractionalHeight(CGFloat) -> Self](./fractionalheight%28_%29.md)
  Creates a dimension that is computed as a fraction of the height of the containing group.
- [class func fractionalWidth(CGFloat) -> Self](./fractionalwidth%28_%29.md)
  Creates a dimension that is computed as a fraction of the width of the containing group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutdimension/estimated(_:))*