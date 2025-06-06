# all

**Framework**: SceneKit  
**Kind**: property

This is the default value for a physics body’s [`collisionBitMask`](scnphysicsbody/collisionbitmask.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var all: SCNPhysicsCollisionCategory { get }
```

#### Discussion

With this collision mask, a physics body can collide with all other physics bodies.

## See Also

- [static var `default`: SCNPhysicsCollisionCategory](scnphysicscollisioncategory/default.md)
  The default [`categoryBitMask`](scnphysicsbody/categorybitmask.md) value for dynamic and kinematic bodies.
- [static var `static`: SCNPhysicsCollisionCategory](scnphysicscollisioncategory/static.md)
  The default [`categoryBitMask`](scnphysicsbody/categorybitmask.md) value for static bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicscollisioncategory/all)*