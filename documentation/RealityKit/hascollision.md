# HasCollision

**Framework**: RealityKit  
**Kind**: protocol

An interface used for ray casting and collision detection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasCollision : HasTransform
```

## Topics

### Getting the component
- [var collision: CollisionComponent?](hascollision/collision.md)
  The collision component that gives the entity the ability to participate in collision simulations.

## Relationships

### Inherits From
- [HasTransform](hastransform.md)
### Inherited By
- [HasPhysics](hasphysics.md)
- [HasPhysicsBody](hasphysicsbody.md)
### Conforming Types
- [ModelEntity](modelentity.md)
- [TriggerVolume](triggervolume.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hascollision)*