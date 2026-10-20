# MeshDeformer

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

An interface for all deformation types in a deformation definition, both built-in and custom. The users overrides all functions to implement a custom `MeshDeformer`, and can in general ignore all but the constructors for built-in deformers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol MeshDeformer : Decodable, Encodable, Equatable, Sendable
```

## Topics

### Identifying the deformer
- [static var type: String](./meshdeformer/type-swift.type.property.md)
  Provide a unique identifier for type of deformer. There can only be one `deform` function associated with each type String. However, each `deform` can vary greatly based on run time options and input.
- [var type: String](./meshdeformer/type-nxsx.md)
  provide a unique identifier for type of deformer, default implementation provided
### Configuring deformation options
- [var options: MeshDeformerOptions](./meshdeformer/options.md)
  provide options for the deformer, default implementation is provided
### Deforming the mesh
- [func deform(parameter: MeshDeformParameterGPU, encoder: any MTLComputeCommandEncoder)](./meshdeformer/deform%28parameter,encoder%29.md)
  deform the mesh on the GPU (the preferred method)
- [func deform(parameter: MeshDeformParameterCPU)](./meshdeformer/deform%28parameter%29.md)
  deform the mesh on the CPU (may be useful for debugging), a no-op is allowed, default implementation is provided
### Comparing deformers
- [func isDeformerEqual(other: any MeshDeformer) -> Bool](./meshdeformer/isdeformerequal%28other%29.md)
  default implementation is provided
### Instance Properties
- [var mode: MeshDeformerExecutionMode](./meshdeformer/mode-6ci1w.md)
  specify which `deform` function will be called, default implementation is provided
### Type Properties
- [static var mode: MeshDeformerExecutionMode](./meshdeformer/mode-v9mj.md)
  specify which `deform` function will be called, default implementation is provided

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [BlendShapeDeformer](./blendshapedeformer.md)
- [BoundingBoxCalculator](./boundingboxcalculator.md)
- [RenormalizingDeformer](./renormalizingdeformer.md)
- [SkinningDeformer](./skinningdeformer.md)
- [SubdivisionSurfaceDeformer](./subdivisionsurfacedeformer.md)

## See Also

### Deformers
- [struct MeshDeformerComponent](./meshdeformercomponent.md)
  The component that applies mesh deformations to an `Entity`.
- [struct SkinningDeformer](./skinningdeformer.md)
  A deformation that binds a 3D mesh to an underlying skeleton.
- [struct BlendShapeDeformer](./blendshapedeformer.md)
  A blend-shape deformation that interpolates between N meshes according to a weighted sum. Consumes information from the `BlendShapeWeightsComponent`


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformer)*