# isHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the item is currently displayed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). As an optimization, the collection view might not create the corresponding view if this property is set to [`true`](../../Swift/true.md).

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
- [var transform: CGAffineTransform](./transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](./alpha.md)
  The transparency of the item.
- [var zIndex: Int](./zindex.md)
  Specifies the item’s position on the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/ishidden)*