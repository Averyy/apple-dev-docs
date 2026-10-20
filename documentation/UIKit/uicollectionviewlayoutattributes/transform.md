# transform

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The affine transform of the item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var transform: CGAffineTransform { get set }
```

```objc
@property (nonatomic) CGAffineTransform transform;
```

#### Discussion

Assigning a value to this property replaces the value in the [`transform3D`](./transform3d.md) property with a 3D version of the affine transform you specify.

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
- [var transform3D: CATransform3D](./transform3d.md)
  The 3D transform of the item.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the item.
- [var zIndex: Int](./zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](./ishidden.md)
  Determines whether the item is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/transform)*