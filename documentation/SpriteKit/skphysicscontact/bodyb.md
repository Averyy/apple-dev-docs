# bodyB

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The second body in the contact.

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
var bodyB: SKPhysicsBody { get }
```

```objc
@property (nonatomic, readonly) SKPhysicsBody * bodyB;
```

## See Also

### Inspecting the Contact Properties
- [var bodyA: SKPhysicsBody](./bodya.md)
  The first body in the contact.
- [var contactPoint: CGPoint](./contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](./collisionimpulse.md)
  The impulse that specifies how hard these two bodies struck each other in Newton-seconds.
- [var contactNormal: CGVector](./contactnormal.md)
  The normal vector specifying the direction of the collision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontact/bodyb)*