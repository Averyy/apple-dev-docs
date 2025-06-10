# setOrientation(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Sets the orientation of the entity relative to the given reference entity.

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
@preconcurrency func setOrientation(_ orientation: simd_quatf, relativeTo referenceEntity: Entity?)
```

## Parameters

- `orientation`: A new orientation, relative to  .
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [var orientation: simd_quatf](hastransform/orientation.md)
  The rotation of the entity relative to its parent.
- [func orientation(relativeTo: Entity?) -> simd_quatf](hastransform/orientation(relativeto:).md)
  Gets the orientation of an entity relative to the given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/setorientation(_:relativeto:))*