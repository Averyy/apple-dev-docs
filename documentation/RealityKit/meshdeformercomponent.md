# MeshDeformerComponent

**Framework**: RealityKit  
**Kind**: struct

The component that applies mesh deformations to an `Entity`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MeshDeformerComponent
```

## Topics

### Configuring deformations
- [var deformations: [MeshDeformationStack]](meshdeformercomponent/deformations.md)
  the deformations applied the entity
### Initializers
- [init(from: [MeshDeformationStack]) throws](meshdeformercomponent/init(from:).md)
  Validates the deformation and throws errors if a configuration problem is detected.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [protocol MeshDeformer](meshdeformer.md)
  An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.
- [struct SkinningDeformer](skinningdeformer.md)
  A deformation that binds a 3D mesh to an underlying skeleton.
- [struct BlendShapeDeformer](blendshapedeformer.md)
  A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`
- [struct OpenSubdivisionDeformer](opensubdivisiondeformer.md)
  OpenSubdiv surface deformation
- [struct RenormalizationDeformer](renormalizationdeformer.md)
  Recalculates tangent frame based on current state of positions
- [struct CalculateBoundingBoxDeformer](calculateboundingboxdeformer.md)
  Calculates a bounding box based on the current state of the deformed positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformercomponent)*