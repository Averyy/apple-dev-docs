# center

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The center point of the dynamic item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var center: CGPoint { get set }
```

```objc
@property (nonatomic, readwrite) CGPoint center;
```

#### Discussion

The dynamic animator (that the item is associated with) calls this method when it has computed a new center point for the item.

## See Also

### Participating in dynamic animation
- [var bounds: CGRect](./bounds.md)
  Called when a dynamic animator needs the bounds of the dynamic item.
- [var transform: CGAffineTransform](./transform.md)
  The rotation of the dynamic item.
- [var collisionBoundsType: UIDynamicItemCollisionBoundsType](./collisionboundstype.md)
  The type of collision bounds associated with the item.
- [var collisionBoundingPath: UIBezierPath](./collisionboundingpath.md)
  The path-based shape to use for the collision bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitem/center)*