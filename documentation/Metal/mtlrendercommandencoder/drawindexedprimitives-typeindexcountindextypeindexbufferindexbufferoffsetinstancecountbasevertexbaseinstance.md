# drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)
```

#### Discussion

You can complete a primitive and start a new one by passing a sentinel index value that’s the largest unsigned integer possible for `indexType`. For example, the largest unsigned integer for [`MTLIndexType.uint16`](mtlindextype/uint16.md) and [`MTLIndexType.uint32`](mtlindextype/uint32.md) is `0xFFFF` and `0xFFFFFFFF`, respectively. The command finishes the current primitive and begins drawing a new one each time the command reads a sentinel index value.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `primitiveType`: An [`MTLPrimitiveType`](mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [`setVertexBuffer(_:offset:index:)`](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.
- `indexCount`: An integer that represents the number of vertices the command reads from `indexBuffer` for each instance.
- `indexType`: An [`MTLIndexType`](mtlindextype.md) instance that represents the index’s format, including [`MTLIndexType.uint16`](mtlindextype/uint16.md) and [`MTLIndexType.uint32`](mtlindextype/uint32.md).
- `indexBuffer`: An [`MTLBuffer`](mtlbuffer.md) instance that contains the `indexCount` vertex indices of the `indexType` format.
- `indexBufferOffset`: An integer that represents the location that’s a multiple of the index size from the start of `indexBuffer` where the vertex indices begin.
- `instanceCount`: An integer that represents the number of times the command draws `primitiveType` with `indexCount` vertices.
- `baseVertex`: The lowest value the command passes to your vertex shader’s parameter with the `vertex_id` attribute. The command assigns each vertex a unique `vertex_id` value that increases from `baseVertex` through `(baseVertex + indexCount - 1)`. Your shader can use that value to identify each vertex in the `primitiveType` instance. For more information about the `vertex_id` argument attribute for vertex shaders, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).
- `baseInstance`: The lowest value the command passes to your vertex shader’s parameter with the `instance_id` attribute. The command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`. Your shader can use that value to identify which instance the vertex belongs to. For more information about the `instance_id` argument attribute for vertex shaders, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:).md)
  Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, instanceCount: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(type: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: any MTLBuffer, indexBufferOffset: Int, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawindexedprimitives(type:indexcount:indextype:indexbuffer:indexbufferoffset:instancecount:basevertex:baseinstance:))*