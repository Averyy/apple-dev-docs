# HasPhysics

**Framework**: RealityKit  
**Kind**: protocol

An interface that combines the physics body and physics motion interfaces.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPhysics : HasPhysicsBody, HasPhysicsMotion
```

## Relationships

### Inherits From
- [HasCollision](hascollision.md)
- [HasPhysicsBody](hasphysicsbody.md)
- [HasPhysicsMotion](hasphysicsmotion.md)
- [HasTransform](hastransform.md)
### Conforming Types
- [ModelEntity](modelentity.md)

## See Also

- [protocol HasPhysicsBody](hasphysicsbody.md)
  An interface that enables physics simulations based on the rules of Newtonian mechanics.
- [protocol HasPhysicsMotion](hasphysicsmotion.md)
  An interface that provides velocity properties for physics simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysics)*