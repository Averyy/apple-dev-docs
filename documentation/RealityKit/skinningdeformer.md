# SkinningDeformer

**Framework**: RealityKit  
**Kind**: struct

A deformation that binds a 3D mesh to an underlying skeleton.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SkinningDeformer
```

## Topics

### Creating a deformer
- [init(skinsTangentFrame: Bool)](skinningdeformer/init(skinstangentframe:).md)
### Configuring tangent skinning
- [var skinsTangentFrame: Bool](skinningdeformer/skinstangentframe.md)
  Specifies whether to skin normals, tangents, and bitangents.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [MeshDeformer](meshdeformer.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MeshDeformerComponent](meshdeformercomponent.md)
  The component that applies mesh deformations to an `Entity`.
- [protocol MeshDeformer](meshdeformer.md)
  An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.
- [struct BlendShapeDeformer](blendshapedeformer.md)
  A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`
- [struct OpenSubdivisionDeformer](opensubdivisiondeformer.md)
  OpenSubdiv surface deformation
- [struct RenormalizationDeformer](renormalizationdeformer.md)
  Recalculates tangent frame based on current state of positions
- [struct CalculateBoundingBoxDeformer](calculateboundingboxdeformer.md)
  Calculates a bounding box based on the current state of the deformed positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skinningdeformer)*