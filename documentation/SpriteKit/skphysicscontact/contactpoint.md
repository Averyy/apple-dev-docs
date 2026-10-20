# contactPoint

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The contact point between the two physics bodies, in scene coordinates.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var contactPoint: CGPoint { get }
```

```objc
@property (nonatomic, readonly) CGPoint contactPoint;
```

## See Also

### Inspecting the Contact Properties
- [var bodyA: SKPhysicsBody](./bodya.md)
  The first body in the contact.
- [var bodyB: SKPhysicsBody](./bodyb.md)
  The second body in the contact.
- [var collisionImpulse: CGFloat](./collisionimpulse.md)
  The impulse that specifies how hard these two bodies struck each other in Newton-seconds.
- [var contactNormal: CGVector](./contactnormal.md)
  The normal vector specifying the direction of the collision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontact/contactpoint)*