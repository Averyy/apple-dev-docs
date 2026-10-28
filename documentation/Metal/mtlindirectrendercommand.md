# MTLIndirectRenderCommand

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

A render command in an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIndirectRenderCommand : NSObjectProtocol
```

```objc
@protocol MTLIndirectRenderCommand <NSObject>
```

## Overview

Don’t implement this protocol; you get instances of this type by asking an [`MTLIndirectCommandBuffer`](./mtlindirectcommandbuffer.md) for them.

Use this instance to reset or encode a command. You need to reset a command before encoding a new command.

## Topics

### Setting command arguments
- [func setRenderPipelineState(any MTLRenderPipelineState)](./mtlindirectrendercommand/setrenderpipelinestate%28_%29.md)
  Sets the render pipeline state for the command.
- [func setVertexBuffer(any MTLBuffer, offset: Int, at: Int)](./mtlindirectrendercommand/setvertexbuffer%28_,offset,at%29.md)
  Sets a vertex buffer argument for the command.
- [func setFragmentBuffer(any MTLBuffer, offset: Int, at: Int)](./mtlindirectrendercommand/setfragmentbuffer%28_,offset,at%29.md)
  Sets a fragment buffer argument for the command.
### Encoding a drawing command
- [func drawPrimitives(MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](./mtlindirectrendercommand/drawprimitives%28_,vertexstart,vertexcount,instancecount,baseinstance%29.md)
  Encodes a command to render a number of instances of primitives using vertex data in contiguous array elements, starting from the base instance.
- [func drawIndexedPrimitives(MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](./mtlindirectrendercommand/drawindexedprimitives%28_,indexcount,indextype,indexbuffer,indexbufferoffset,instancecount,basevertex,baseinstance%29.md)
  Encodes a command to render a number of instances of primitives using an index list specified in a buffer, starting from the base vertex of the base instance.
- [func drawPatches(Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int, tessellationFactorBuffer: any MTLBuffer, tessellationFactorBufferOffset: Int, tessellationFactorBufferInstanceStride: Int)](./mtlindirectrendercommand/drawpatches%28_,patchstart,patchcount,patchindexbuffer,patchindexbufferoffset,instancecount,baseinstance,tessellationfactorbuffer,tessellationfactorbufferoffset,tessellationfactorbufferinstancestride%29.md)
  Encodes a command to render a number of instances of tessellated patches.
- [func drawIndexedPatches(Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, controlPointIndexBuffer: any MTLBuffer, controlPointIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int, tessellationFactorBuffer: any MTLBuffer, tessellationFactorBufferOffset: Int, tessellationFactorBufferInstanceStride: Int)](./mtlindirectrendercommand/drawindexedpatches%28__patchstart_patchcount_patchindexbuffer_patchindexbufferoffset_controlpointindexbuffer_controlpointindexbufferoffset_instancecount_baseinstance_tessellationfactorbuffer_tessellationfactorbufferoffse-1368a335.md)
  Encodes a command to render a number of instances of tessellated patches, using a control point index buffer.
### Resetting a command
- [func reset()](./mtlindirectrendercommand/reset%28%29.md)
  Resets the command to its default state.
### Instance Methods
- [func clearBarrier()](./mtlindirectrendercommand/clearbarrier%28%29.md)
- [func drawMeshThreadgroups(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./mtlindirectrendercommand/drawmeshthreadgroups%28_,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
- [func drawMeshThreads(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](./mtlindirectrendercommand/drawmeshthreads%28_,threadsperobjectthreadgroup,threadspermeshthreadgroup%29.md)
- [func setBarrier()](./mtlindirectrendercommand/setbarrier%28%29.md)
- [func setCullMode(MTLCullMode)](./mtlindirectrendercommand/setcullmode%28_%29.md)
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./mtlindirectrendercommand/setdepthbias%28_,slopescale,clamp%29.md)
- [func setDepthClipMode(MTLDepthClipMode)](./mtlindirectrendercommand/setdepthclipmode%28_%29.md)
- [func setDepthStencilState((any MTLDepthStencilState)?)](./mtlindirectrendercommand/setdepthstencilstate%28_%29.md)
- [func setFrontFacing(MTLWinding)](./mtlindirectrendercommand/setfrontfacing%28_%29.md)
- [func setMeshBuffer(any MTLBuffer, offset: Int, at: Int)](./mtlindirectrendercommand/setmeshbuffer%28_,offset,at%29.md)
- [func setObjectBuffer(any MTLBuffer, offset: Int, at: Int)](./mtlindirectrendercommand/setobjectbuffer%28_,offset,at%29.md)
- [func setObjectThreadgroupMemoryLength(Int, index: Int)](./mtlindirectrendercommand/setobjectthreadgroupmemorylength%28_,index%29.md)
- [func setTriangleFillMode(MTLTriangleFillMode)](./mtlindirectrendercommand/settrianglefillmode%28_%29.md)
- [func setVertexBuffer(any MTLBuffer, offset: Int, attributeStride: Int, at: Int)](./mtlindirectrendercommand/setvertexbuffer%28_,offset,attributestride,at%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Render compute commands
- [struct MTLDrawPatchIndirectArguments](./mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawPrimitivesIndirectArguments](./mtldrawprimitivesindirectarguments.md)
  The data layout required for drawing primitives via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](./mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand)*