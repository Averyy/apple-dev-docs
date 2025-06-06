# MTLRenderCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An interface that encodes a render pass into a command buffer, including all its draw calls and configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLRenderCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Improving Rendering Performance with Vertex Amplification](improving-rendering-performance-with-vertex-amplification.md)
- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)
- [Setting Up a Command Structure](setting-up-a-command-structure.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

The [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) protocol defines an interface that configures and encodes a render pass. Use a render pass to draw a scene, or a component within a scene, to its render , the outputs of a render pass. You can use various approaches to render to those outputs, including techniques that apply the following:

- Primitive drawing
- Mesh drawing
- Ray tracing
- Tile shaders dispatching

To create an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance, call the [`makeRenderCommandEncoder(descriptor:)`](mtlcommandbuffer/makerendercommandencoder(descriptor:).md) of an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance, or the [`makeRenderCommandEncoder()`](mtlparallelrendercommandencoder/makerendercommandencoder().md) method of an [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) instance.

To configure the render pass for your first drawing commands, start with a pipeline state by passing an [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instance to the encoder’s [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method. You create the pipeline states your render pass needs, typically ahead of time, by calling one or more [`MTLDevice`](mtldevice.md) methods (see [`Pipeline State Creation`](pipeline-state-creation.md)).

> 💡 **Tip**:  Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

 Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

Set any other applicable parts of the encoder’s configuration by calling the methods on the [`Render Pass Configuration`](render-pass-configuration.md) page. For example, you may need to configure the pass’s viewport, its scissor rectangle, and the settings for depth and stencil tests.

Assign resources, such as buffers and textures, for the shaders that depend on them. For more information, see the shader-specific pages in the resource preparation section, such as [`Vertex Shader Resource Preparation Commands`](vertex-shader-resource-preparation-commands.md) and [`Fragment Shader Resource Preparation Commands`](fragment-shader-resource-preparation-commands.md). If your shaders access resources through an argument buffer, ensure the pass makes those resources  by loading those resources resident in GPU memory. You do this by calling the methods on the [`Argument Buffer Resource Preparation Commands`](argument-buffer-resource-preparation-commands.md) page.

Encode drawing commands by calling the methods on the [`Render Pass Drawing Commands`](render-pass-drawing-commands.md) page after you configure the state and resources the commands depend on. The encoder maintains its current state and applies them to all subsequent draw commands. For drawing commands that need different states or resources, reconfigure the render pass appropriately and then encode those draw commands. Repeat the process for each batch of drawing commands that depend on the same render pass configuration and resources.

When you finish encoding the render pass’s commands, finalize it into the command buffer by calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method.

## Topics

### Encoding Configuration Commands
- [Render Pass Configuration](render-pass-configuration.md)
  Set a render pass’s pipeline state, attachment actions, viewports, and so on, that affect subsequent drawing commands.
### Encoding Resource Preparation Commands
- [Mesh and Object Shader Resource Preparation Commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex Shader Resource Preparation Commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment Shader Resource Preparation Commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile Shaders Resource Preparation Commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument Buffer Resource Preparation Commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
### Encoding Draw Commands
- [Render Pass Drawing Commands](render-pass-drawing-commands.md)
  Render an image by drawing meshes, primitives, tessellation patches, and by dispatching tile shaders.
### Encoding Resource Synchronization Commands
- [func waitForFence(any MTLFence, before: MTLRenderStages)](mtlrendercommandencoder/waitforfence(_:before:).md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [func updateFence(any MTLFence, after: MTLRenderStages)](mtlrendercommandencoder/updatefence(_:after:).md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which signals passes waiting on the fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(scope:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
### Encoding Commands that Run Indirect Command Buffers
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlrendercommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes a command that runs a range of commands from an indirect command buffer (ICB).
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).
### Encoding Data Sampling Commands
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command that samples hardware counters during the render pass and stores the data into a counter sample buffer.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Methods
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:).md)
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:).md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:).md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:attributestride:index:).md)

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum MTLTriangleFillMode](mtltrianglefillmode.md)
  Specifies how to rasterize triangle and triangle strip primitives.
- [enum MTLWinding](mtlwinding.md)
  The vertex winding rule that determines a front-facing primitive.
- [enum MTLCullMode](mtlcullmode.md)
  The mode that determines whether to perform culling and which type of primitive to cull.
- [enum MTLPrimitiveType](mtlprimitivetype.md)
  The geometric primitive type for drawing commands.
- [enum MTLIndexType](mtlindextype.md)
  The index type for an index buffer that references vertices of geometric primitives.
- [enum MTLDepthClipMode](mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultMode](mtlvisibilityresultmode.md)
  The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder)*