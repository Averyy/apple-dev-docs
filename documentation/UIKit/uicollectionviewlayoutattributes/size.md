# size

**Framework**: UIKit  
**Kind**: property

The size of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var size: CGSize { get set }
```

#### Discussion

Setting the value of this property also changes the size of the rectangle returned by the [`frame`](uicollectionviewlayoutattributes/frame.md) and [`bounds`](uicollectionviewlayoutattributes/bounds.md) properties.

## See Also

- [var frame: CGRect](uicollectionviewlayoutattributes/frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](uicollectionviewlayoutattributes/bounds.md)
  The bounds of the item.
- [var center: CGPoint](uicollectionviewlayoutattributes/center.md)
  The center point of the item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/size)*