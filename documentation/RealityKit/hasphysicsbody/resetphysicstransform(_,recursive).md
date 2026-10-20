# resetPhysicsTransform(_:recursive:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resets the position and velocities of the simulated physics body.

**Availability**:
- iOS 13.0+ - Deprecated (renamed: resetPhysicsTransform(recursive:))
- iPadOS 13.0+ - Deprecated (renamed: resetPhysicsTransform(recursive:))
- Mac Catalyst 13.0+ - Deprecated (renamed: resetPhysicsTransform(recursive:))
- macOS 10.15+ - Deprecated (renamed: resetPhysicsTransform(recursive:))
- visionOS 1.0+ - Deprecated (renamed: resetPhysicsTransform(recursive:))

## Declaration

```swift
@MainActor
@preconcurrency func resetPhysicsTransform(_ transform: Transform, recursive: Bool = true)
```

#### Discussion

Call this method to change the transform applied to a body by physics simulation. This only matters for dynamic rigid bodies, with a [`mode`](../physicsbodycomponent/mode.md) of [`PhysicsBodyMode.dynamic`](../physicsbodymode/dynamic.md). This is the only kind of body that’s affected by physics simulations. For all others, modify the entity’s [`transform`](../hastransform/transform.md) property directly.

Conversely, directly modifying the transform of a dynamic body has no effect because the physics simulation overwrites it on every frame.

## Parameters

- `transform`: The new transform to inject into the dynamic physics simulation of the entity.
- `recursive`: Apply the reset to child entities.

## See Also

### Resetting physics simulations
- [func resetPhysicsTransform(recursive: Bool)](./resetphysicstransform%28recursive%29.md)
  Resets the position, orientation, and velocities of the simulated physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/resetphysicstransform(_:recursive:))*