# center

**Framework**: UIKit  
**Kind**: property

The center point of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var center: CGPoint { get set }
```

#### Discussion

The center point is specified in the coordinate system of the collection view. Setting the value of this property also updates the origin of the rectangle in the [`frame`](uicollectionviewlayoutattributes/frame.md) property.

## See Also

- [var frame: CGRect](uicollectionviewlayoutattributes/frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](uicollectionviewlayoutattributes/bounds.md)
  The bounds of the item.
- [var size: CGSize](uicollectionviewlayoutattributes/size.md)
  The size of the item.
- [var transform3D: CATransform3D](uicollectionviewlayoutattributes/transform3d.md)
  The 3D transform of the item.
- [var transform: CGAffineTransform](uicollectionviewlayoutattributes/transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](uicollectionviewlayoutattributes/alpha.md)
  The transparency of the item.
- [var zIndex: Int](uicollectionviewlayoutattributes/zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](uicollectionviewlayoutattributes/ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/center)*