# scale(relativeTo:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Gets the scale of an entity relative to the given entity.

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
@preconcurrency func scale(relativeTo referenceEntity: Entity?) -> SIMD3<Float>
```

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set this to `nil` to indicate world space.

## See Also

### Scaling an entity
- [var scale: SIMD3<Float>](./scale.md)
  The scale of the entity relative to its parent.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](./setscale%28_,relativeto%29.md)
  Sets the scale factor of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/scale(relativeto:))*