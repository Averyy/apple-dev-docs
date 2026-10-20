# categoryBitMask

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A mask that defines which categories this physics body belongs to.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var categoryBitMask: Int { get set }
```

```objc
@property (nonatomic) NSUInteger categoryBitMask;
```

#### Discussion

Every physics body in a scene can be assigned to one or more categories, each corresponding to a bit in the bit mask. You define the mask values used in your game. Use this property together with the [`physicsShape`](./physicsshape.md) and [`contactTestBitMask`](./contacttestbitmask.md) properties to define which physics bodies interact with each other and when your game is notified of interactions.

The default value is [`static`](../scnphysicscollisioncategory/static.md) for static bodies and [`default`](../scnphysicscollisioncategory/default.md) for dynamic and kinematic bodies.

## See Also

### Working with Contacts and Collisions
- [var contactTestBitMask: Int](./contacttestbitmask.md)
  A mask that defines which categories of bodies cause intersection notifications with this physics body.
- [var collisionBitMask: Int](./collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [struct SCNPhysicsCollisionCategory](../scnphysicscollisioncategory.md)
  Default values for a physics body’s [`categoryBitMask`](./categorybitmask.md) and [`collisionBitMask`](./collisionbitmask.md) properties.
- [var continuousCollisionDetectionThreshold: CGFloat](./continuouscollisiondetectionthreshold.md)
  The minimum distance the body must travel for SceneKit to apply a more precise (but more costly) algorithm to detect contacts with other bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/categorybitmask)*