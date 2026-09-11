# MeshDeformerOptions

**Framework**: RealityKit  
**Kind**: struct

Specifies constant options for `MeshDeformer`

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MeshDeformerOptions
```

## Topics

### Creating deformer options
- [init(cadence: MeshDeformerOptions.Cadence, inputSpec: MeshDeformerVertexOptions, outputSpec: MeshDeformerVertexOptions)](meshdeformeroptions/init(cadence:inputspec:outputspec:).md)
  specify your own cadence and read / write options
### Specifying vertex data
- [let inputSpec: MeshDeformerVertexOptions](meshdeformeroptions/inputspec.md)
  The expected vertex buffer input spec for the deformer type.
- [let outputSpec: MeshDeformerVertexOptions](meshdeformeroptions/outputspec.md)
  The expected vertex buffer output spec for the deformer type.
### Configuring the cadence
- [let cadence: MeshDeformerOptions.Cadence](meshdeformeroptions/cadence-swift.property.md)
  Determines the update frequence for the defomer type.
- [MeshDeformerOptions.Cadence](meshdeformeroptions/cadence-swift.enum.md)
  Specifies when RealityKit applies the custom deformer functions.
### Initializers
- [init()](meshdeformeroptions/init.md)
  defaults to on demand, and reads and writes positions only

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct MeshDeformerVertexOptions](meshdeformervertexoptions.md)
  MeshDeformerVertexOptions allows developers to specify which vertex types in the mesh to allocate in the input and output buffers for mesh deformations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformeroptions)*