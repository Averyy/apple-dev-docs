# orientation(relativeTo:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Gets the orientation of an entity relative to the given entity.

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
@preconcurrency func orientation(relativeTo referenceEntity: Entity?) -> simd_quatf
```

## Return Value

The orientation of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set this to `nil` to indicate world space.

## See Also

### Rotating an entity
- [var orientation: simd_quatf](./orientation.md)
  The rotation of the entity relative to its parent.
- [func setOrientation(simd_quatf, relativeTo: Entity?)](./setorientation%28_,relativeto%29.md)
  Sets the orientation of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/orientation(relativeto:))*