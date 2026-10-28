# collisionBoundingPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The path-based shape to use for the collision bounds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional var collisionBoundingPath: UIBezierPath { get }
```

```objc
@property (nonatomic, readonly) UIBezierPath * collisionBoundingPath;
```

## Discussion

When the [`collisionBoundsType`](./collisionboundstype.md) property is [`UIDynamicItemCollisionBoundsType.path`](../uidynamicitemcollisionboundstype/path.md), the object in this property is used as the collision bounds. If your dynamic item implements the [`collisionBoundsType`](./collisionboundstype.md) property, you must also implement this property.

The path object you create must represent a convex polygon with counter-clockwise or clockwise winding, and the path must not intersect itself. The (0, 0) point of the path must be located at the [`center`](./center.md) point of the corresponding dynamic item. If the center point does not match the path’s origin, collision behaviors may not work as expected.

## See Also

### Participating in dynamic animation
- [var bounds: CGRect](./bounds.md)
  Called when a dynamic animator needs the bounds of the dynamic item.
- [var center: CGPoint](./center.md)
  The center point of the dynamic item.
- [var transform: CGAffineTransform](./transform.md)
  The rotation of the dynamic item.
- [var collisionBoundsType: UIDynamicItemCollisionBoundsType](./collisionboundstype.md)
  The type of collision bounds associated with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitem/collisionboundingpath)*