# drawIndexedPrimitives(type:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

#### Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [`MTLBuffer`](mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

You can complete a primitive and start a new one by passing a sentinel index value that’s the largest unsigned integer possible for `indexType`. For example, the largest unsigned integer for [`MTLIndexType.uint16`](mtlindextype/uint16.md) and [`MTLIndexType.uint32`](mtlindextype/uint32.md) is `0xFFFF` and `0xFFFFFFFF`, respectively. The command finishes the current primitive and begins drawing a new one each time the command reads a sentinel index value.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `primitiveType`: See the   method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.
- `indexType`: An   instance that represents the index’s format, including   and  .
- `indexBuffer`: An   instance that contains the vertex indices of the   format.
- `indexBufferOffset`: An integer that represents the location that’s a multiple of the index size from the start of   where the vertex indices begin.
- `indirectBuffer`: An   instance with data that matches the layout of the   structure.
- `indirectBufferOffset`: See the   to check for offset alignment requirements for buffers in   and   address space.

## See Also

- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:).md)
  Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:))*