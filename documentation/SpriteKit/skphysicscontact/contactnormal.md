# contactNormal

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The normal vector specifying the direction of the collision.

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
var contactNormal: CGVector { get }
```

```objc
@property (nonatomic, readonly) CGVector contactNormal;
```

## See Also

### Inspecting the Contact Properties
- [var bodyA: SKPhysicsBody](./bodya.md)
  The first body in the contact.
- [var bodyB: SKPhysicsBody](./bodyb.md)
  The second body in the contact.
- [var contactPoint: CGPoint](./contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](./collisionimpulse.md)
  The impulse that specifies how hard these two bodies struck each other in Newton-seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontact/contactnormal)*