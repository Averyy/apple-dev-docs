# MeshDeformerVertexOptions

**Framework**: RealityKit  
**Kind**: struct

MeshDeformerVertexOptions allows developers to specify which vertex types in the mesh to allocate in the input and output buffers for mesh deformations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MeshDeformerVertexOptions
```

## Topics

### Specifying geometric attributes
- [static var positions: MeshDeformerVertexOptions](meshdeformervertexoptions/positions.md)
  Specifies positions only.
- [static var normals: MeshDeformerVertexOptions](meshdeformervertexoptions/normals.md)
  Specifies normals only.
- [static var tangents: MeshDeformerVertexOptions](meshdeformervertexoptions/tangents.md)
  Specifies tangents only.
- [static var bitangents: MeshDeformerVertexOptions](meshdeformervertexoptions/bitangents.md)
  Specifies bitangents only.
- [static var tangentFrame: MeshDeformerVertexOptions](meshdeformervertexoptions/tangentframe.md)
  Specifies all of the normalizable vertex types.
### Specifying texture coordinates
- [static var uvs: MeshDeformerVertexOptions](meshdeformervertexoptions/uvs.md)
  Specifies uvs only.
- [static var uv1s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv1s.md)
  Specifies uv1s only.
- [static var uv2s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv2s.md)
  Specifies uv2s only.
- [static var uv3s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv3s.md)
  Specifies uv3s only.
- [static var uv4s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv4s.md)
  Specifies uv4s only.
- [static var uv5s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv5s.md)
  Specifies uv5s only.
- [static var uv6s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv6s.md)
  Specifies uv6s only.
- [static var uv7s: MeshDeformerVertexOptions](meshdeformervertexoptions/uv7s.md)
  Specifies uv7s only.
### Storing option values
- [MeshDeformerVertexOptions.OptionStorage](meshdeformervertexoptions/optionstorage.md)
### Type Properties
- [static var all: MeshDeformerVertexOptions](meshdeformervertexoptions/all.md)
  Specifies all  vertex types.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct MeshDeformerOptions](meshdeformeroptions.md)
  Specifies constant options for `MeshDeformer`
- [enum MeshDeformerExecutionMode](meshdeformerexecutionmode.md)
  Specifies which `MesDeformer.deform` function will be called when used with custom deformers.
- [struct MeshDeformParameter](meshdeformparameter.md)
  Base class for GPU and CPU custom deform function input
- [struct MeshDeformationStack](meshdeformationstack.md)
  A set of `MeshDeformer`s to apply in order to a mesh, or a proper subset of the mesh specified by `Target`s. If at any point, a deformer in the stack updates, all deformers later in the stack will also update.
- [struct MeshScope](meshscope.md)
  The elements of a mesh resource that a deformation stack applies to.
- [typealias MeshDeformParameterCPU](meshdeformparametercpu.md)
  convenience alias
- [typealias MeshDeformParameterGPU](meshdeformparametergpu.md)
  convenience alias
- [typealias MeshDeformParametersCPU](meshdeformparameterscpu.md)
  convenience alias
- [typealias MeshDeformParametersGPU](meshdeformparametersgpu.md)
  convenience alias
- [typealias MeshDeformCPUBufferInput](meshdeformcpubufferinput.md)
  The underlying type of deformer input data buffers for the CPU functions.
- [typealias MeshDeformGPUBufferInput](meshdeformgpubufferinput.md)
  The underlying type of deformer input data buffers for the GPU functions.
- [typealias MeshDeformCPUBufferOutput](meshdeformcpubufferoutput.md)
  The underlying type of deformer output data buffers for the CPU functions.
- [typealias MeshDeformGPUBufferOutput](meshdeformgpubufferoutput.md)
  The underlying type of deformer input data buffers for the GPU functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformervertexoptions)*