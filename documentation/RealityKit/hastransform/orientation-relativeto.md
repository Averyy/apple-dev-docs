# orientation(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the orientation of an entity relative to the given entity.

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
@preconcurrency func orientation(relativeTo referenceEntity: Entity?) -> simd_quatf
```

#### Return Value

The orientation of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [var orientation: simd_quatf](hastransform/orientation.md)
  The rotation of the entity relative to its parent.
- [func setOrientation(simd_quatf, relativeTo: Entity?)](hastransform/setorientation(_:relativeto:).md)
  Sets the orientation of the entity relative to the given reference entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/orientation(relativeto:))*