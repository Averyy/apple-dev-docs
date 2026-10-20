# drawPrimitives(type:vertexStart:vertexCount:instanceCount:baseInstance:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)
```

#### Discussion

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `primitiveType`: An [`MTLPrimitiveType`](mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [`setVertexBuffer(_:offset:index:)`](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.
- `vertexStart`: The lowest value the command passes to your vertex shader’s parameter with the `vertex_id` attribute. The command assigns each vertex a unique `vertex_id` value within its drawing instance that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`. Your shader can use that value to identify a vertex in each drawing instance. For more information about the `vertex_id` argument attribute for vertex shaders, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).
- `vertexCount`: An integer that represents the number of vertices of `primitiveType` the command draws per instance.
- `instanceCount`: An integer that represents the number of times the command draws `primitiveType` with `vertexCount` vertices.
- `baseInstance`: The lowest value the command passes to your vertex shader’s parameter with the `instance_id` attribute. The command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`. Your shader can use that value to identify which instance the vertex belongs to. For more information about the `instance_id` argument attribute for vertex shaders, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:))*