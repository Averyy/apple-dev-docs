# move(to:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Moves an entity instantly to a new location given by a transform.

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
@preconcurrency func move(to transform: Transform, relativeTo referenceEntity: Entity?)
```

## Parameters

- `transform`: A   instance that indicates the new location.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [func move(to: float4x4, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6jul8.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?)](hastransform/look(at:from:upvector:relativeto:).md)
  Positions and orients the entity to look at a target from a given position.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?, forward: Entity.ForwardDirection)](hastransform/look(at:from:upvector:relativeto:forward:).md)
  Positions and orients the entity such that it looks at certain target from a give position.
- [func align(GeometricPin, to: GeometricPin) -> float4x4?](hastransform/align(_:to:).md)
  Moves and rotates the entity by a transformation from the origin pin to the target pin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/move(to:relativeto:)-6lohd)*