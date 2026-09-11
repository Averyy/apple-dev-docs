# MeshDeformerComponent

**Framework**: RealityKit  
**Kind**: struct

The component that applies mesh deformations to an `Entity`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol MeshDeformer](meshdeformer.md)
  An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.
- [struct SkinningDeformer](skinningdeformer.md)
  A deformation that binds a 3D mesh to an underlying skeleton.
- [struct BlendShapeDeformer](blendshapedeformer.md)
  A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformercomponent)*