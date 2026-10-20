# SCNPhysicsCollisionCategory

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Default values for a physics body’s [`categoryBitMask`](./scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](./scnphysicsbody/collisionbitmask.md) properties.

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
struct SCNPhysicsCollisionCategory
```

```c
enum SCNPhysicsCollisionCategory : NSUInteger;
```

#### Overview

You specify contact and collision behaviors by defining your own categories for the kinds of bodies your app simulates and setting the [`categoryBitMask`](./scnphysicsbody/categorybitmask.md) and [`collisionBitMask`](./scnphysicsbody/collisionbitmask.md) properties for each body to determine which kinds of bodies it collides with. Additionally, you can use the [`contactDelegate`](./scnphysicsworld/contactdelegate.md) property of the physics world to be notified of collisions between bodies.

For more details and example usage, see [Defining a Body’s Category and Collisions](./scnphysicsbody.md#Defining-a-Bodys-Category-and-Collisions) in the class overview.

## Topics

### Constants
- [static var `default`: SCNPhysicsCollisionCategory](./scnphysicscollisioncategory/default.md)
  The default [`categoryBitMask`](./scnphysicsbody/categorybitmask.md) value for dynamic and kinematic bodies.
- [static var `static`: SCNPhysicsCollisionCategory](./scnphysicscollisioncategory/static.md)
  The default [`categoryBitMask`](./scnphysicsbody/categorybitmask.md) value for static bodies.
- [static var all: SCNPhysicsCollisionCategory](./scnphysicscollisioncategory/all.md)
  This is the default value for a physics body’s [`collisionBitMask`](./scnphysicsbody/collisionbitmask.md) property.
### Initializers
- [init(rawValue: UInt)](./scnphysicscollisioncategory/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Working with Contacts and Collisions
- [var categoryBitMask: Int](./scnphysicsbody/categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var contactTestBitMask: Int](./scnphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of bodies cause intersection notifications with this physics body.
- [var collisionBitMask: Int](./scnphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var continuousCollisionDetectionThreshold: CGFloat](./scnphysicsbody/continuouscollisiondetectionthreshold.md)
  The minimum distance the body must travel for SceneKit to apply a more precise (but more costly) algorithm to detect contacts with other bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory)*