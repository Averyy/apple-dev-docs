# bounds

**Framework**: UIKit  
**Kind**: property

The bounds of the item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bounds: CGRect { get set }
```

#### Discussion

When setting the bounds, the origin of the bounds rectangle must always be at (0, 0). Changing the bounds rectangle also changes the value in the [`size`](uicollectionviewlayoutattributes/size.md) property to match the new bounds size.

## See Also

- [var frame: CGRect](uicollectionviewlayoutattributes/frame.md)
  The frame rectangle of the item.
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
- [var zIndex: Int](uicollectionviewlayoutattributes/zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](uicollectionviewlayoutattributes/ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/bounds)*