# MTLIndirectRenderCommand

**Framework**: Metal  
**Kind**: protocol

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

#### Overview

Don’t implement this protocol; you get objects of this type by asking a [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) for them.

Use this object to reset or encode a command. You must always reset a command before encoding a new command.

## Topics

### Setting Command Arguments
- [func setRenderPipelineState(any MTLRenderPipelineState)](mtlindirectrendercommand/setrenderpipelinestate(_:).md)
  Sets the render pipeline state object used by the command.
- [func setVertexBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setvertexbuffer(_:offset:at:).md)
  Sets a vertex buffer argument for the command.
- [func setFragmentBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setfragmentbuffer(_:offset:at:).md)
  Sets a fragment buffer argument for the command.
### Encoding a Drawing Command
- [func drawPrimitives(MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtlindirectrendercommand/drawprimitives(_:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a command to render a number of instances of primitives using vertex data in contiguous array elements, starting from the base instance.
- [func drawIndexedPrimitives(MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtlindirectrendercommand/drawindexedprimitives(_:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:).md)
  Encodes a command to render a number of instances of primitives using an index list specified in a buffer, starting from the base vertex of the base instance.
- [func drawPatches(Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int, tessellationFactorBuffer: any MTLBuffer, tessellationFactorBufferOffset: Int, tessellationFactorBufferInstanceStride: Int)](mtlindirectrendercommand/drawpatches(_:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:instancecount:baseinstance:tessellationfactorbuffer:tessellationfactorbufferoffset:tessellationfactorbufferinstancestride:).md)
  Encodes a command to render a number of instances of tessellated patches.
- [func drawIndexedPatches(Int, patchStart: Int, patchCount: Int, patchIndexBuffer: (any MTLBuffer)?, patchIndexBufferOffset: Int, controlPointIndexBuffer: any MTLBuffer, controlPointIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int, tessellationFactorBuffer: any MTLBuffer, tessellationFactorBufferOffset: Int, tessellationFactorBufferInstanceStride: Int)](mtlindirectrendercommand/drawindexedpatches(_:patchstart:patchcount:patchindexbuffer:patchindexbufferoffset:controlpointindexbuffer:controlpointindexbufferoffset:instancecount:baseinstance:tessellationfactorbuffer:tessellationfactorbufferoffset:tessellationfactorbu-4mdz8.md)
  Encodes a command to render a number of instances of tessellated patches, using a control point index buffer.
### Resetting a Command
- [func reset()](mtlindirectrendercommand/reset.md)
  Resets the command to its default state.
### Instance Methods
- [func clearBarrier()](mtlindirectrendercommand/clearbarrier.md)
- [func drawMeshThreadgroups(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlindirectrendercommand/drawmeshthreadgroups(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
- [func drawMeshThreads(MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)](mtlindirectrendercommand/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md)
- [func setBarrier()](mtlindirectrendercommand/setbarrier.md)
- [func setMeshBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setmeshbuffer(_:offset:at:).md)
- [func setObjectBuffer(any MTLBuffer, offset: Int, at: Int)](mtlindirectrendercommand/setobjectbuffer(_:offset:at:).md)
- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtlindirectrendercommand/setobjectthreadgroupmemorylength(_:index:).md)
- [func setVertexBuffer(any MTLBuffer, offset: Int, attributeStride: Int, at: Int)](mtlindirectrendercommand/setvertexbuffer(_:offset:attributestride:at:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md)
  The data layout required for drawing primitives via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand)*