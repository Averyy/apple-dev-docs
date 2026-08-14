# ComputeNodeGraph.Assembly

**Framework**: Compute Graph  
**Kind**: struct

Fully assembled configuration of compute graph nodes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
struct Assembly
```

#### Overview

You can create an assembly from a ComputeNodeGraph to obtain the layout of all buffers and uniforms needed by the graph.

Unless you need the layout before or without compiling the shaders, you can compile [`ComputeNodeGraph.Pipelines`](computenodegraph/pipelines.md) directly from a [`ComputeNodeGraph`](computenodegraph.md).

## Topics

### Structures
- [ComputeNodeGraph.Assembly.BufferBinding](computenodegraph/assembly/bufferbinding.md)
  Describes how a Metal buffer is bound to a compute pipeline stage.
- [ComputeNodeGraph.Assembly.TextureBinding](computenodegraph/assembly/texturebinding.md)
  Describes how a Metal texture is bound to a compute pipeline stage.
- [ComputeNodeGraph.Assembly.UniformBinding](computenodegraph/assembly/uniformbinding.md)
  Describes how a uniform value is located within the graph’s uniform buffer.
### Initializers
- [init(ComputeNodeGraph) throws](computenodegraph/assembly/init(_:).md)
### Instance Properties
- [var constantBuffers: [ComputeNodeGraph.Assembly.BufferBinding]](computenodegraph/assembly/constantbuffers.md)
- [var deviceBuffers: [ComputeNodeGraph.Assembly.BufferBinding]](computenodegraph/assembly/devicebuffers.md)
- [var namedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding]](computenodegraph/assembly/nameduniforms.md)
  Uniforms that are named and exposed as parameters of this graph, keyed by name.
- [var sharedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding]](computenodegraph/assembly/shareduniforms.md)
  Uniforms that are shared across multiple graphs, keyed by typeName.
- [var textures: [ComputeNodeGraph.Assembly.TextureBinding]](computenodegraph/assembly/textures.md)
- [var uniformBufferSize: Int](computenodegraph/assembly/uniformbuffersize.md)
- [var uniforms: [ComputeNodeGraph.Port.Address : ComputeNodeGraph.Assembly.Location]](computenodegraph/assembly/uniforms.md)
### Enumerations
- [ComputeNodeGraph.Assembly.Attachment](computenodegraph/assembly/attachment.md)
  Identifies where a resource is attached in the compute graph.
- [ComputeNodeGraph.Assembly.Location](computenodegraph/assembly/location.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly)*