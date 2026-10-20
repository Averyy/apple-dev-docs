# frame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The frame rectangle of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var frame: CGRect { get set }
```

```objc
@property (nonatomic) CGRect frame;
```

#### Discussion

The frame rectangle is measured in points and specified in the coordinate system of the collection view. Setting the value of this property also sets the values of the [`center`](./center.md) and [`size`](./size.md) properties.

## See Also

### Accessing the layout attributes
- [var bounds: CGRect](./bounds.md)
  The bounds of the item.
- [var center: CGPoint](./center.md)
  The center point of the item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/frame)*