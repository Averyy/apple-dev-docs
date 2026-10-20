# transform3D

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The 3D transform of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var transform3D: CATransform3D { get set }
```

```objc
@property (nonatomic) CATransform3D transform3D;
```

#### Discussion

Assigning a value to this property replaces the value in the [`transform`](./transform.md) property with an affine version of the 3D transform you specify.

## See Also

### Accessing the layout attributes
- [var frame: CGRect](./frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](./bounds.md)
  The bounds of the item.
- [var center: CGPoint](./center.md)
  The center point of the item.
- [var size: CGSize](./size.md)
  The size of the item.
- [var transform: CGAffineTransform](./transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the item.
- [var zIndex: Int](./zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](./ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/transform3d)*