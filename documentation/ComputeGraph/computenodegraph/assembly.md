# ComputeNodeGraph.Assembly

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Fully assembled configuration of compute graph nodes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct Assembly
```

#### Overview

You can create an assembly from a ComputeNodeGraph to obtain the layout of all buffers and uniforms needed by the graph.

Unless you need the layout before or without compiling the shaders, you can compile [`ComputeNodeGraph.Pipelines`](./pipelines.md) directly from a [`ComputeNodeGraph`](../computenodegraph.md).

## Topics

### Structures
- [ComputeNodeGraph.Assembly.BufferBinding](./assembly/bufferbinding.md)
  Describes how a Metal buffer is bound to a compute pipeline stage.
- [ComputeNodeGraph.Assembly.TextureBinding](./assembly/texturebinding.md)
  Describes how a Metal texture is bound to a compute pipeline stage.
- [ComputeNodeGraph.Assembly.UniformBinding](./assembly/uniformbinding.md)
  Describes how a uniform value is located within the graph’s uniform buffer.
### Initializers
- [init(ComputeNodeGraph) throws](./assembly/init%28_%29.md)
### Instance Properties
- [var constantBuffers: [ComputeNodeGraph.Assembly.BufferBinding]](./assembly/constantbuffers.md)
- [var deviceBuffers: [ComputeNodeGraph.Assembly.BufferBinding]](./assembly/devicebuffers.md)
- [var namedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding]](./assembly/nameduniforms.md)
  Uniforms that are named and exposed as parameters of this graph, keyed by name.
- [var sharedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding]](./assembly/shareduniforms.md)
  Uniforms that are shared across multiple graphs, keyed by typeName.
- [var textures: [ComputeNodeGraph.Assembly.TextureBinding]](./assembly/textures.md)
- [var uniformBufferSize: Int](./assembly/uniformbuffersize.md)
- [var uniforms: [ComputeNodeGraph.Port.Address : ComputeNodeGraph.Assembly.Location]](./assembly/uniforms.md)
### Enumerations
- [ComputeNodeGraph.Assembly.Attachment](./assembly/attachment.md)
  Identifies where a resource is attached in the compute graph.
- [ComputeNodeGraph.Assembly.Location](./assembly/location.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Graph definition and assembly
- [struct ComputeNodeGraph](../computenodegraph.md)
- [ComputeNodeGraph.Pipelines](./pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](./pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](./nodedefinition.md)
- [ComputeNodeGraph.Library](./library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](./libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly)*