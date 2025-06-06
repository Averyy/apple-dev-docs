# align(_:to:)

**Framework**: RealityKit  
**Kind**: method

Moves and rotates the entity by a transformation from the origin pin to the target pin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func align(_ originPin: GeometricPin, to targetPin: GeometricPin) -> float4x4?
```

#### Return Value

Transformation matrix that has been applied to the `Entity`, in the frame or reference of the parent of the `Entity`. If either pin doesn’t exist, returns `nil`.

## Parameters

- `originPin`: The   to align. It should be one of the pins on the entity.
- `targetPin`: The   to align to.

## See Also

- [func move(to: Transform, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6lohd.md)
  Moves an entity instantly to a new location given by a transform.
- [func move(to: float4x4, relativeTo: Entity?)](hastransform/move(to:relativeto:)-6jul8.md)
  Moves an entity instantly to a new location given by a 4x4 matrix.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?)](hastransform/look(at:from:upvector:relativeto:).md)
  Positions and orients the entity to look at a target from a given position.
- [func look(at: SIMD3<Float>, from: SIMD3<Float>, upVector: SIMD3<Float>, relativeTo: Entity?, forward: Entity.ForwardDirection)](hastransform/look(at:from:upvector:relativeto:forward:).md)
  Positions and orients the entity such that it looks at certain target from a give position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/align(_:to:))*