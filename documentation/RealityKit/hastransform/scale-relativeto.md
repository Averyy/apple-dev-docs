# scale(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the scale of an entity relative to the given entity.

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
@preconcurrency func scale(relativeTo referenceEntity: Entity?) -> SIMD3<Float>
```

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [var scale: SIMD3<Float>](hastransform/scale.md)
  The scale of the entity relative to its parent.
- [func setScale(SIMD3<Float>, relativeTo: Entity?)](hastransform/setscale(_:relativeto:).md)
  Sets the scale factor of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/scale(relativeto:))*