# collisionImpulse

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The impulse that specifies how hard these two bodies struck each other in Newton-seconds.

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
var collisionImpulse: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat collisionImpulse;
```

## See Also

### Inspecting the Contact Properties
- [var bodyA: SKPhysicsBody](./bodya.md)
  The first body in the contact.
- [var bodyB: SKPhysicsBody](./bodyb.md)
  The second body in the contact.
- [var contactPoint: CGPoint](./contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var contactNormal: CGVector](./contactnormal.md)
  The normal vector specifying the direction of the collision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontact/collisionimpulse)*