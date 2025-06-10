# zIndex

**Framework**: UIKit  
**Kind**: property

Specifies the item’s position on the z axis.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var zIndex: Int { get set }
```

#### Discussion

This property is used to determine the front-to-back ordering of items during layout. Items with higher index values appear on top of items with lower values. Items with the same value have an undetermined order.

The default value of this property is 0.

## See Also

- [var frame: CGRect](uicollectionviewlayoutattributes/frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](uicollectionviewlayoutattributes/bounds.md)
  The bounds of the item.
- [var center: CGPoint](uicollectionviewlayoutattributes/center.md)
  The center point of the item.
- [var size: CGSize](uicollectionviewlayoutattributes/size.md)
  The size of the item.
- [var transform3D: CATransform3D](uicollectionviewlayoutattributes/transform3d.md)
  The 3D transform of the item.
- [var transform: CGAffineTransform](uicollectionviewlayoutattributes/transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](uicollectionviewlayoutattributes/alpha.md)
  The transparency of the item.
- [var isHidden: Bool](uicollectionviewlayoutattributes/ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/zindex)*