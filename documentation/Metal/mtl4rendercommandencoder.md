# MTL4RenderCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes configuration and draw commands for a single render pass into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4RenderCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

A render pass draws a scene, or a component within a scene, to its render , the outputs of a render pass. You can render to those outputs with various approaches, including techniques that apply the following:

- Primitive drawing
- Mesh drawing
- Ray tracing
- Dispatching tile shaders

Create a render encoder by calling a factory method of an [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance, such as [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md).

To configure the render pass for your first drawing commands, start with a pipeline state by passing an [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instance to the encoder’s [`setRenderPipelineState(_:)`](mtl4rendercommandencoder/setrenderpipelinestate(_:).md) method. You create the pipeline states your render pass needs, typically ahead of time, by calling one or more [`MTLDevice`](mtldevice.md) methods (see [`Pipeline state creation`](pipeline-state-creation.md)).

> 💡 **Tip**:  Avoid visual stutter by creating pipeline states at a noncritical time, such as during launch, because of the time it can take to make them.

Configure other encoder settings by calling the methods in the configuration groups below, such as [`setViewport(_:)`](mtl4rendercommandencoder/setviewport(_:).md) for the viewport, [`setScissorRect(_:)`](mtl4rendercommandencoder/setscissorrect(_:).md) for the scissor rectangle, and [`setDepthStencilState(_:)`](mtl4rendercommandencoder/setdepthstencilstate(_:).md) for depth and stencil tests.

Bind resources by calling [`setArgumentTable(_:stages:)`](mtl4rendercommandencoder/setargumenttable(_:stages:).md) with an [`MTL4ArgumentTable`](mtl4argumenttable.md) instance. This table contains the buffers, textures, and other resources your shaders depend on.

Encode drawing commands after you configure the state and resources the commands depend on. The encoder maintains its current state and applies it to all subsequent draw commands. For drawing commands that need different states or resources, reconfigure the render pass appropriately and then encode those draw commands. Repeat the process for each batch of drawing commands that depend on the same render pass configuration and resources.

When you finish encoding the render pass’s commands, finalize it into the command buffer by calling the encoder’s [`endEncoding()`](mtl4commandencoder/endencoding().md) method.

##### Command Stages

Most render commands apply to one or more stages within a pass. The following table shows which stages apply to each command:

| Function | MTLStages |
| --- | --- |
| [`drawPrimitives(primitiveType:vertexStart:vertexCount:)`](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:)`](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:baseInstance:)`](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawPrimitives(primitiveType:indirectBuffer:)`](mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:)`](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:)`](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:)`](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:basevertex:baseinstance:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawIndexedPrimitives(primitiveType:indexType:indexBuffer:indexBufferLength:indirectBuffer:)`](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indextype:indexbuffer:indexbufferlength:indirectbuffer:).md) | [`vertex`](mtlstages/vertex.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreads(threadsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`drawMeshThreadgroups(indirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md) | [`object`](mtlstages/object.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`mesh`](mtlstages/mesh.md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`fragment`](mtlstages/fragment.md) |
| [`dispatchThreadsPerTile(_:)`](mtl4rendercommandencoder/dispatchthreadspertile(_:).md) | [`tile`](mtlstages/tile.md) |
| [`executeCommands(buffer:range:)`](mtl4rendercommandencoder/executecommands(buffer:range:).md)![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png)[`executeCommandsInBuffer:withRange:`](mtl4rendercommandencoder/executecommandsinbuffer:withrange:.md) | None |
| [`executeCommands(buffer:indirectBuffer:)`](mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:).md) | None |
| [`writeTimestamp(granularity:after:counterHeap:index:)`](mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:).md) | None |

Draw commands don’t apply to [`fragment`](mtlstages/fragment.md) when the [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) for the draw disables rasterization. See [`isRasterizationEnabled`](mtl4renderpipelinedescriptor/israsterizationenabled.md).

Mesh draw commands don’t apply to [`object`](mtlstages/object.md) when the [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) for the draw doesn’t have an object shader.

The [`executeCommands(buffer:range:)`](mtl4rendercommandencoder/executecommands(buffer:range:).md) and [`executeCommands(buffer:indirectBuffer:)`](mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:).md) commands don’t apply to any stage, which means you can’t use a barrier to wait for all commands in an indirect command buffer to complete. However, each command within the [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) applies to the same stages as when you encode the equivalent command directly.

For more information about stages and synchronization, see [`MTLStages`](mtlstages.md) and [`Resource synchronization`](resource-synchronization.md).

## Topics

### Configuring pipeline state
- [func setRenderPipelineState(any MTLRenderPipelineState)](mtl4rendercommandencoder/setrenderpipelinestate(_:).md)
  Configures this encoder with a render pipeline state that applies to your subsequent draw commands.
### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](mtl4rendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
### Configuring blend behavior
- [func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)](mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:).md)
  Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
- [func setColorAttachmentMap(MTLLogicalToPhysicalColorAttachmentMap?)](mtl4rendercommandencoder/setcolorattachmentmap(_:).md)
  Sets the mapping from logical shader color output to physical render pass color attachments.
### Configuring rendering behavior
- [func setTriangleFillMode(MTLTriangleFillMode)](mtl4rendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setFrontFacing(MTLWinding)](mtl4rendercommandencoder/setfrontfacing(_:).md)
  Configures the vertex winding order that determines which face of a geometric primitive is the front one.
- [func setCullMode(MTLCullMode)](mtl4rendercommandencoder/setcullmode(_:).md)
  Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.
### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtl4rendercommandencoder/setdepthclipmode(_:).md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setDepthTestBounds(ClosedRange<Float>)](mtl4rendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(_:).md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(front:back:).md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](mtl4rendercommandencoder/setviewport(_:).md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [func setViewports([MTLViewport])](mtl4rendercommandencoder/setviewports(_:).md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setScissorRect(MTLScissorRect)](mtl4rendercommandencoder/setscissorrect(_:).md)
  Sets a scissor rectangle to discard fragments outside a specific area.
- [func setScissorRects([MTLScissorRect])](mtl4rendercommandencoder/setscissorrects(_:).md)
  Sets an array of scissor rectangles for a fragment scissor test.
### Configuring visibility testing
- [func setVisibilityResultMode(MTLVisibilityResultMode, offset: Int)](mtl4rendercommandencoder/setvisibilityresultmode(_:offset:).md)
  Configures a visibility test for Metal to run, and the destination for any results it generates.
### Configuring vertex amplification
- [func setVertexAmplificationCount(Int)](mtl4rendercommandencoder/setvertexamplificationcount(_:)-85tu1.md)
  Sets the vertex amplification count and its view mapping for each amplification ID.
- [func setVertexAmplificationCount([MTLVertexAmplificationViewMapping])](mtl4rendercommandencoder/setvertexamplificationcount(_:)-911ja.md)
  Sets the vertex amplification count and its view mapping for each amplification ID.
### Configuring persistent threadgroup memory
- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.
- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.
### Binding argument tables
- [func setArgumentTable(any MTL4ArgumentTable, stages: MTLRenderStages)](mtl4rendercommandencoder/setargumenttable(_:stages:).md)
  Associates an argument table with a set of render stages.
### Drawing with vertices
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
### Drawing with indexed vertices
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:).md)
  Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, instanceCount: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:basevertex:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indextype:indexbuffer:indexbufferlength:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.
### Drawing with meshes
- [func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [func drawMeshThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.
### Drawing with tile shaders
- [func dispatchThreadsPerTile(MTLSize)](mtl4rendercommandencoder/dispatchthreadspertile(_:).md)
  Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.
- [var tileWidth: Int](mtl4rendercommandencoder/tilewidth.md)
  Sets the width of a tile for this render pass.
- [var tileHeight: Int](mtl4rendercommandencoder/tileheight.md)
  Sets the height of a tile for this render pass.
### Running commands from indirect command buffers
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4rendercommandencoder/executecommands(buffer:range:).md)
  Encodes a command that runs a range of commands from an indirect command buffer.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:).md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer.
### Sampling counters
- [func writeTimestamp(granularity: MTL4TimestampGranularity, after: MTLRenderStages, counterHeap: any MTL4CounterHeap, index: Int)](mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:).md)
  Writes a GPU timestamp into the given [`MTL4CounterHeap`](mtl4counterheap.md) at `index` after `stage` completes.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLRenderCommandEncoder](mtlrendercommandencoder.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder)*