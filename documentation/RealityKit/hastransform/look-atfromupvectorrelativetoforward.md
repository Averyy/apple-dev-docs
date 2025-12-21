# look(at:from:upVector:relativeTo:forward:)

**Framework**: RealityKit  
**Kind**: method

Positions and orients the entity such that it looks at certain target from a give position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func look(at target: SIMD3<Float>, from position: SIMD3<Float>, upVector: SIMD3<Float> = SIMD3<Float>(0, 1, 0), relativeTo referenceEntity: Entity?, forward: Entity.ForwardDirection = .negativeZ)
```

#### Discussion

This function moves the entity to the specified `position`. It rotates the entity such that the forward direction is pointing towards `target`. It further makes sure that entity’s  direction aligns with the specified `upVector`.

> **Note**: This method can be used for non-camera entities.

## Parameters

- `target`: The target position to look at.
- `position`: The new position of the entity.
- `upVector`: The   direction of the entity.
- `referenceEntity`: The reference entity which defines the frame of reference.   Can be  , which is equivalent to “world space”.
- `forward`: Use default forward (.negativeZ).   Can be set to .positiveZ for non-camera entities

## See Also

- [func move(to: Transform, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6lohd.md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6jul8.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?)](hastransform/look(at:from:upvector:relativeto:).md)
  Positions and orients the entity to look at a target from a given position.
- [func align(GeometricPin, to: GeometricPin) -> float4x4?](hastransform/align(_:to:).md)
  Moves and rotates the entity by a transformation from the origin pin to the target pin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/look(at:from:upvector:relativeto:forward:))*