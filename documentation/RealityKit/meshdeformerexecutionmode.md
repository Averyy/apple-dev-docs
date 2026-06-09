# MeshDeformerExecutionMode

**Framework**: RealityKit  
**Kind**: enum

Specifies which `MesDeformer.deform` function will be called when used with custom deformers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum MeshDeformerExecutionMode
```

## Topics

### Choosing an execution mode
- [MeshDeformerExecutionMode.gpu](meshdeformerexecutionmode/gpu.md)
  specifies calling `MeshDeformer.deform(parameter: MeshDeformParameterGPU, encoder: any MTLComputeCommandEncoder)`
- [MeshDeformerExecutionMode.cpu](meshdeformerexecutionmode/cpu.md)
  specifies calling `MeshDeformer.deform(parameter: MeshDeformParameterCPU)`

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MeshDeformerOptions](meshdeformeroptions.md)
  Specifies constant options for `MeshDeformer`
- [struct MeshDeformerVertexOptions](meshdeformervertexoptions.md)
  MeshDeformerVertexOptions allows developers to specify which vertex types in the mesh to allocate in the input and output buffers for mesh deformations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformerexecutionmode)*