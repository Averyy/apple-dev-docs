# MTLRenderCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes configuration and draw commands for a single render pass into a command buffer.

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

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Improving rendering performance with vertex amplification](improving-rendering-performance-with-vertex-amplification.md)
- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Setting up a command structure](setting-up-a-command-structure.md)
- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)

#### Overview

A render pass draws a scene, or a component within a scene, to its render , the outputs of a render pass. You can render to those outputs with various approaches, including techniques that apply the following:

- Primitive drawing
- Mesh drawing
- Ray tracing
- Dispatching tile shaders

To create an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance, call the [`makeRenderCommandEncoder(descriptor:)`](mtlcommandbuffer/makerendercommandencoder(descriptor:).md) method of an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance, or the [`makeRenderCommandEncoder()`](mtlparallelrendercommandencoder/makerendercommandencoder().md) method of an [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) instance.

To configure the render pass for your first drawing commands, start with a pipeline state by passing an [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instance to the encoder’s [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method. You create the pipeline states your render pass needs, typically ahead of time, by calling one or more [`MTLDevice`](mtldevice.md) methods (see [`Pipeline state creation`](pipeline-state-creation.md)).

> 💡 **Tip**:  Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

Configure other encoder settings by calling the methods on the [`Render pass configuration`](render-pass-configuration.md) page. For example, you may need to configure the pass’s viewport, its scissor rectangle, and the settings for depth and stencil tests.

Assign resources, such as buffers and textures, for the shaders that depend on them. For more information, see the shader-specific pages in the resource preparation section, such as [`Vertex shader resource preparation commands`](vertex-shader-resource-preparation-commands.md) and [`Fragment shader resource preparation commands`](fragment-shader-resource-preparation-commands.md). If your shaders access resources through an argument buffer, make those resources  in GPU memory by calling the methods on the [`Argument buffer resource preparation commands`](argument-buffer-resource-preparation-commands.md) page.

Encode drawing commands after you configure the state and resources the commands depend on. The encoder maintains its current state and applies it to all subsequent draw commands. For drawing commands that need different states or resources, reconfigure the render pass appropriately and then encode those draw commands. Repeat the process for each batch of drawing commands that depend on the same render pass configuration and resources.

When you finish encoding the render pass’s commands, finalize it into the command buffer by calling the encoder’s [`endEncoding()`](mtlcommandencoder/endencoding().md) method.

##### Command Stages

Most render commands apply to one or more stages within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
| --- | --- |
| [`drawPrimitives(type:vertexStart:vertexCount:)`](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(type:vertexStart:vertexCount:instanceCount:)`](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(type:vertexStart:vertexCount:instanceCount:baseInstance:)`](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(type:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:)`](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:)`](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(type:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreads(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtlrendercommandencoder/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreadgroups(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtlrendercommandencoder/drawmeshthreadgroups(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreadgroups(indirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer:indirectbufferoffset:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPatches(numberOfPatchControlPoints:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:)`](mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:instancecount:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:indirectbuffer:indirectbufferoffset:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPatches(numberOfPatchControlPoints:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:)`](mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:instancecount:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:indirectbuffer:indirectbufferoffset:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`dispatchThreadsPerTile(_:)`](mtlrendercommandencoder/dispatchthreadspertile(_:).md) | [`tile`](mtlstages/tile.md) |
| [`executeCommandsInBuffer(_:range:)`](mtlrendercommandencoder/executecommandsinbuffer(_:range:).md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`executeCommandsInBuffer:withRange:`](mtlrendercommandencoder/executecommandsinbuffer:withrange:.md) | None |
| [`executeCommandsInBuffer(_:indirectBuffer:offset:)`](mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:`](mtlrendercommandencoder/executecommandsinbuffer:indirectbuffer:indirectbufferoffset:.md) | None |
| [`sampleCounters(sampleBuffer:sampleIndex:barrier:)`](mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md) | None |

Draw commands don’t apply to [`fragment`](mtlstages/fragment.md) when the [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) for the draw disables rasterization. See [`isRasterizationEnabled`](mtlrenderpipelinedescriptor/israsterizationenabled.md).

Mesh draw commands don’t apply to [`object`](mtlstages/object.md) when the [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) for the draw doesn’t have an object shader.

The [`executeCommandsInBuffer(_:range:)`](mtlrendercommandencoder/executecommandsinbuffer(_:range:).md) and [`executeCommandsInBuffer(_:indirectBuffer:offset:)`](mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

> **Note**: [`MTLRenderStages`](mtlrenderstages.md) and its values have the same functionality as [`MTLStages`](mtlstages.md) and its corresponding stage values.

For more information about stages and synchronization, see [`MTLStages`](mtlstages.md) and [`Resource synchronization`](resource-synchronization.md).

## Topics

### Configuration commands
- [Render pass configuration](render-pass-configuration.md)
  Set a render pass’s pipeline state, attachment actions, viewports, and so on, that affect subsequent drawing commands.
### Resource preparation commands
- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.
### Drawing with vertices
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.
- [func drawPrimitives(type: MTLPrimitiveType, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
### Drawing with indexed vertices
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:).md)
  Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.
### Drawing with meshes
- [func drawMeshThreads(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlrendercommandencoder/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlrendercommandencoder/drawmeshthreadgroups(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [func drawMeshThreadgroups(indirectBuffer: any MTLBuffer, indirectBufferOffset: Int, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlrendercommandencoder/drawmeshthreadgroups(indirectbuffer:indirectbufferoffset:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.
### Drawing with tessellation patches
- [func drawPatches(numberOfPatchControlPoints: Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of tessellated patches.
- [func drawPatches(numberOfPatchControlPoints: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of tessellated patches with indirect arguments.
### Drawing with indexed tessellation patches
- [func drawIndexedPatches(numberOfPatchControlPoints: Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, controlPointIndexBuffer: any MTLBuffer, controlPointIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer.
- [func drawIndexedPatches(numberOfPatchControlPoints: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, controlPointIndexBuffer: any MTLBuffer, controlPointIndexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawindexedpatches(numberofpatchcontrolpoints:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of tessellated patches with a control point index buffer and indirect arguments.
### Drawing with tile shaders
- [func dispatchThreadsPerTile(MTLSize)](mtlrendercommandencoder/dispatchthreadspertile(_:).md)
  Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.
- [var tileWidth: Int](mtlrendercommandencoder/tilewidth.md)
  The width of the tiles, in pixels, for the render command encoder.
- [var tileHeight: Int](mtlrendercommandencoder/tileheight.md)
  The height of the tiles, in pixels, for the render command encoder.
### Preventing resource access conflicts
- [func waitForFence(any MTLFence, before: MTLRenderStages)](mtlrendercommandencoder/waitforfence(_:before:).md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [func updateFence(any MTLFence, after: MTLRenderStages)](mtlrendercommandencoder/updatefence(_:after:).md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(scope:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.
### Running commands from indirect command buffers
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, range: Range<Int>)](mtlrendercommandencoder/executecommandsinbuffer(_:range:).md)
  Encodes a command that runs a range of commands from an indirect command buffer (ICB).
- [func executeCommandsInBuffer(any MTLIndirectCommandBuffer, indirectBuffer: any MTLBuffer, offset: Int)](mtlrendercommandencoder/executecommandsinbuffer(_:indirectbuffer:offset:).md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer (ICB).
### Sampling counters
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command that samples hardware counters during the render pass and stores the data into a counter sample buffer.
### Deprecated
- [Deprecated symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTL4RenderCommandEncoder](mtl4rendercommandencoder.md)
  Encodes configuration and draw commands for a single render pass into a command buffer.
- [struct MTL4RenderEncoderOptions](mtl4renderencoderoptions.md)
  Custom render pass options you specify at encoder creation time.
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
- [enum MTLVisibilityResultType](mtlvisibilityresulttype.md)
  This enumeration controls if Metal accumulates visibility results between render encoders or resets them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder)*