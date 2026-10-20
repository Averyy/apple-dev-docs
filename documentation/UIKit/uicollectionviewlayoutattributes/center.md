# center

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The center point of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var center: CGPoint { get set }
```

```objc
@property (nonatomic) CGPoint center;
```

#### Discussion

The center point is specified in the coordinate system of the collection view. Setting the value of this property also updates the origin of the rectangle in the [`frame`](./frame.md) property.

## See Also

### Accessing the layout attributes
- [var frame: CGRect](./frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](./bounds.md)
  The bounds of the item.
- [var size: CGSize](./size.md)
  The size of the item.
- [var transform3D: CATransform3D](./transform3d.md)
  The 3D transform of the item.
- [var transform: CGAffineTransform](./transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the item.
- [var zIndex: Int](./zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](./ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/center)*