# HasPhysicsMotion

**Framework**: RealityKit  
**Kind**: protocol

An interface that provides velocity properties for physics simulations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPhysicsMotion : Entity
```

## Topics

### Setting the motion component
- [var physicsMotion: PhysicsMotionComponent?](hasphysicsmotion/physicsmotion.md)
  The physics motion component used by physics simulations of the model entity.

## Relationships

### Inherits From
- [Entity](entity.md)
### Inherited By
- [HasPhysics](hasphysics.md)
### Conforming Types
- [ModelEntity](modelentity.md)

## See Also

- [protocol HasPhysicsBody](hasphysicsbody.md)
  An interface that enables physics simulations based on the rules of Newtonian mechanics.
- [protocol HasPhysics](hasphysics.md)
  An interface that combines the physics body and physics motion interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsmotion)*