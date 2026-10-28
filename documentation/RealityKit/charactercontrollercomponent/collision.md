# CharacterControllerComponent.Collision

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A container that holds collision state for the character controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Collision
```

## Overview

All coordinates are in *physics space*, the coordinate system of the physics simulation.

## Topics

### Initializers
- [init(characterEntity: Entity, hitEntity: Entity, hitPosition: SIMD3<Float>, hitNormal: SIMD3<Float>, moveDirection: SIMD3<Float>, moveDistance: Float)](./collision/init%28characterentity,hitentity,hitposition,hitnormal,movedirection,movedistance%29.md)
  Create Collision and initialize all fields.
### Instance Properties
- [var characterEntity: Entity](./collision/characterentity.md)
  Entity owning the character controller component.
- [var hitEntity: Entity](./collision/hitentity.md)
  The entity that was hit by the character controller.
- [var hitNormal: SIMD3<Float>](./collision/hitnormal.md)
  Hit normal relative to physics origin. In physics space.
- [var hitPosition: SIMD3<Float>](./collision/hitposition.md)
  Hit position relative to physics origin. In physics space.
- [var moveDirection: SIMD3<Float>](./collision/movedirection.md)
  Move direction controller was moving (unit vector). In physics space.
- [var moveDistance: Float](./collision/movedistance.md)
  Move distance controller was attempting to move. In physics space.

## See Also

### Character control
- [struct CharacterControllerComponent](../charactercontrollercomponent.md)
  A component that manages character movement.
- [CharacterControllerComponent.CollisionFlags](./collisionflags.md)
  An option set that specifies which parts of the character capsule have collided with other objects.
- [struct CharacterControllerStateComponent](../charactercontrollerstatecomponent.md)
  A component that represents the state of a character controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/collision)*