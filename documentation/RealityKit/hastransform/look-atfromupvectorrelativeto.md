# look(at:from:upVector:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Positions and orients the entity to look at a target from a given position.

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
@preconcurrency func look(at target: SIMD3<Float>, from position: SIMD3<Float>, upVector: SIMD3<Float> = SIMD3<Float>(0, 1, 0), relativeTo referenceEntity: Entity?)
```

#### Discussion

You can use this method on any entity, but it’s particularly useful for orienting cameras and lights to aim at a particular point in space.

## Parameters

- `target`: The target position to look at.
- `position`: The new position of the entity.
- `upVector`: The up direction of the entity after moving.
- `referenceEntity`: The entity that defines a frame of reference. Set this to    to indicate world space.

## See Also

- [func move(to: Transform, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6lohd.md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6jul8.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?, forward: Entity.ForwardDirection)](hastransform/look(at:from:upvector:relativeto:forward:).md)
  Positions and orients the entity such that it looks at certain target from a give position.
- [func align(GeometricPin, to: GeometricPin) -> float4x4?](hastransform/align(_:to:).md)
  Moves and rotates the entity by a transformation from the origin pin to the target pin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/look(at:from:upvector:relativeto:))*