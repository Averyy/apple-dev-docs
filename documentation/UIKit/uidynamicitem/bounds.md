# bounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Called when a dynamic animator needs the bounds of the dynamic item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var bounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect bounds;
```

## See Also

### Participating in dynamic animation
- [var center: CGPoint](./center.md)
  The center point of the dynamic item.
- [var transform: CGAffineTransform](./transform.md)
  The rotation of the dynamic item.
- [var collisionBoundsType: UIDynamicItemCollisionBoundsType](./collisionboundstype.md)
  The type of collision bounds associated with the item.
- [var collisionBoundingPath: UIBezierPath](./collisionboundingpath.md)
  The path-based shape to use for the collision bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitem/bounds)*