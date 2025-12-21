# isHidden

**Framework**: UIKit  
**Kind**: property

Determines whether the item is currently displayed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHidden: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). As an optimization, the collection view might not create the corresponding view if this property is set to [`true`](https://developer.apple.com/documentation/Swift/true).

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
- [var zIndex: Int](uicollectionviewlayoutattributes/zindex.md)
  Specifies the item’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/ishidden)*