# transformMatrix(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Gets the 4 x 4 transform matrix of an entity relative to the given entity.

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
@preconcurrency func transformMatrix(relativeTo referenceEntity: Entity?) -> float4x4
```

#### Return Value

The transform of the entity relative to `referenceEntity`.

## Parameters

- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.

## See Also

- [Transforming entities between RealityKit coordinate spaces](transforming-entities-between-realitykit-coordinate-spaces.md)
  Move an entity between a volumetric window and an immersive space using coordinate space transformations.
- [func setTransformMatrix(float4x4, relativeTo: Entity?)](hastransform/settransformmatrix(_:relativeto:).md)
  Sets the transform of the entity relative to the given reference entity using a 4x4 matrix representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/transformmatrix(relativeto:))*