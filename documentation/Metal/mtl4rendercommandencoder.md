# MTL4RenderCommandEncoder

**Framework**: Metal  
**Kind**: protocol

Encodes a render pass into a command buffer, including all its draw calls and configuration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4RenderCommandEncoder : MTL4CommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var tileHeight: Int](mtl4rendercommandencoder/tileheight.md)
  Sets the height of a tile for this render pass.
- [var tileWidth: Int](mtl4rendercommandencoder/tilewidth.md)
  Sets the width of a tile for this render pass.
### Instance Methods
- [func dispatchThreadsPerTile(MTLSize)](mtl4rendercommandencoder/dispatchthreadspertile(_:).md)
  Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:).md)
  Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int, instanceCount: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:basevertex:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int, indirectBuffer: UInt64)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indextype:indexbuffer:indexbufferlength:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.
- [func drawMeshThreadgroups(indirectBuffer: UInt64, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(indirectbuffer:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with indirect arguments.
- [func drawMeshThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threadgroups.
- [func drawMeshThreads(threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtl4rendercommandencoder/drawmeshthreads(threadspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
  Encodes a draw command that invokes a mesh shader and, optionally, an object shader with a grid of threads.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: UInt64)](mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, indirectBuffer: UInt64)](mtl4rendercommandencoder/executecommands(buffer:indirectbuffer:).md)
  Encodes a command that runs an indirect range of commands from an indirect command buffer.
- [func executeCommands(buffer: any MTLIndirectCommandBuffer, range: Range<Int>)](mtl4rendercommandencoder/executecommands(buffer:range:).md)
  Encodes a command that runs a range of commands from an indirect command buffer.
- [func setArgumentTable(any MTL4ArgumentTable, stages: MTLRenderStages)](mtl4rendercommandencoder/setargumenttable(_:stages:).md)
  Associates an argument table with a set of render stages.
- [func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)](mtl4rendercommandencoder/setblendcolor(red:green:blue:alpha:).md)
  Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
- [func setColorAttachmentMap(MTLLogicalToPhysicalColorAttachmentMap)](mtl4rendercommandencoder/setcolorattachmentmap(_:).md)
  Sets the mapping from logical shader color output to physical render pass color attachments.
- [func setColorStoreAction(MTLStoreAction, index: Int)](mtl4rendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setCullMode(MTLCullMode)](mtl4rendercommandencoder/setcullmode(_:).md)
  Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtl4rendercommandencoder/setdepthclipmode(_:).md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setFrontFacing(MTLWinding)](mtl4rendercommandencoder/setfrontfacing(_:).md)
  Configures the vertex winding order that determines which face of a geometric primitive is the front one.
- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.
- [func setRenderPipelineState(any MTLRenderPipelineState)](mtl4rendercommandencoder/setrenderpipelinestate(_:).md)
  Configures this encoder with a render pipeline state that applies to your subsequent draw commands.
- [func setScissorRect(MTLScissorRect)](mtl4rendercommandencoder/setscissorrect(_:).md)
  Sets a scissor rectangle to discard fragments outside a specific area.
- [func setScissorRects([MTLScissorRect])](mtl4rendercommandencoder/setscissorrects(_:).md)
  Sets an array of scissor rectangles for a fragment scissor test.
- [func setStencilReferenceValue(UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(_:).md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(front:back:).md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
- [func setStencilStoreAction(MTLStoreAction)](mtl4rendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:).md)
  Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.
- [func setTriangleFillMode(MTLTriangleFillMode)](mtl4rendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setVertexAmplificationCount(Int)](mtl4rendercommandencoder/setvertexamplificationcount(_:)-85tu1.md)
  Sets the vertex amplification count and its view mapping for each amplification ID.
- [func setVertexAmplificationCount([MTLVertexAmplificationViewMapping])](mtl4rendercommandencoder/setvertexamplificationcount(_:)-911ja.md)
  Sets the vertex amplification count and its view mapping for each amplification ID.
- [func setViewport(MTLViewport)](mtl4rendercommandencoder/setviewport(_:).md)
  Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.
- [func setViewports([MTLViewport])](mtl4rendercommandencoder/setviewports(_:).md)
  Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.
- [func setVisibilityResultMode(MTLVisibilityResultMode, offset: Int)](mtl4rendercommandencoder/setvisibilityresultmode(_:offset:).md)
  Configures a visibility test for Metal to run, and the destination for any results it generates.
- [func writeTimestamp(granularity: MTL4TimestampGranularity, after: MTLRenderStages, counterHeap: any MTL4CounterHeap, index: Int)](mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:).md)
  Writes a GPU timestamp into the given [`MTL4CounterHeap`](mtl4counterheap.md) at `index` after `stage` completes.

## Relationships

### Inherits From
- [MTL4CommandEncoder](mtl4commandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLRenderCommandEncoder](mtlrendercommandencoder.md)
  An interface that encodes a render pass into a command buffer, including all its draw calls and configuration.
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