# resetPhysicsTransform(recursive:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resets the position, orientation, and velocities of the simulated physics body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func resetPhysicsTransform(recursive: Bool = true)
```

#### Discussion

Call this method only for dynamic rigid bodies, with a [`mode`](../physicsbodycomponent/mode.md) of [`PhysicsBodyMode.dynamic`](../physicsbodymode/dynamic.md). This is the only kind of body that’s affected by physics simulations. For all others, modify the entity’s transform property directly.

Conversely, directly modifying the transform of a dynamic body has no effect because the physics simulation overwrites it on every frame.

## Parameters

- `recursive`: Apply the reset to all descendant entities.

## See Also

### Resetting physics simulations
- [func resetPhysicsTransform(Transform, recursive: Bool)](./resetphysicstransform%28_,recursive%29.md)
  Resets the position and velocities of the simulated physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/resetphysicstransform(recursive:))*