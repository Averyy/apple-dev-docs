# BlendShapeDeformer

**Framework**: RealityKit  
**Kind**: struct

A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BlendShapeDeformer
```

## Topics

### Initializers
- [init()](blendshapedeformer/init.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [MeshDeformer](meshdeformer.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct MeshDeformerComponent](meshdeformercomponent.md)
  The component that applies mesh deformations to an `Entity`.
- [protocol MeshDeformer](meshdeformer.md)
  An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.
- [struct SkinningDeformer](skinningdeformer.md)
  A deformation that binds a 3D mesh to an underlying skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapedeformer)*