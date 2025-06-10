# categoryBitMask

**Framework**: SceneKit  
**Kind**: property

A mask that defines which categories this physics body belongs to.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var categoryBitMask: Int { get set }
```

#### Discussion

Every physics body in a scene can be assigned to one or more categories, each corresponding to a bit in the bit mask. You define the mask values used in your game. Use this property together with the [`physicsShape`](scnphysicsbody/physicsshape.md) and [`contactTestBitMask`](scnphysicsbody/contacttestbitmask.md) properties to define which physics bodies interact with each other and when your game is notified of interactions.

The default value is [`static`](scnphysicscollisioncategory/static.md) for static bodies and [`default`](scnphysicscollisioncategory/default.md) for dynamic and kinematic bodies.

## See Also

- [var contactTestBitMask: Int](scnphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of bodies cause intersection notifications with this physics body.
- [var collisionBitMask: Int](scnphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [struct SCNPhysicsCollisionCategory](scnphysicscollisioncategory.md)
  Default values for a physics body’s [`categoryBitMask`](scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) properties.
- [var continuousCollisionDetectionThreshold: CGFloat](scnphysicsbody/continuouscollisiondetectionthreshold.md)
  The minimum distance the body must travel for SceneKit to apply a more precise (but more costly) algorithm to detect contacts with other bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/categorybitmask)*