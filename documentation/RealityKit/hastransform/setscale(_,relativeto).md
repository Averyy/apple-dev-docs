# setScale(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the scale factor of the entity relative to the given reference entity.

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
@preconcurrency func setScale(_ scale: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `scale`: A new scale factor, relative to `referenceEntity`.
- `referenceEntity`: The entity that defines a frame of reference. Set this to `nil` to indicate world space.

## See Also

### Scaling an entity
- [var scale: SIMD3<Float>](./scale.md)
  The scale of the entity relative to its parent.
- [func scale(relativeTo: Entity?) -> SIMD3<Float>](./scale%28relativeto%29.md)
  Gets the scale of an entity relative to the given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/setscale(_:relativeto:))*