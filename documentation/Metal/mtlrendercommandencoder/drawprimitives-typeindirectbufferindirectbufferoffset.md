# drawPrimitives(type:indirectBuffer:indirectBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func drawPrimitives(type primitiveType: MTLPrimitiveType, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)
```

#### Discussion

Indirect drawing methods may help your app avoid expensive latency costs. This is because the command reads arguments from an [`MTLBuffer`](mtlbuffer.md) instance instead of using the CPU to pass parameters to the command.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `primitiveType`: An [`MTLPrimitiveType`](mtlprimitivetype.md) instance that represents how the command interprets vertex argument data. See the [`setVertexBuffer(_:offset:index:)`](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md) method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.
- `indirectBuffer`: An [`MTLBuffer`](mtlbuffer.md) instance with data that matches the layout of the [`MTLDrawPrimitivesIndirectArguments`](mtldrawprimitivesindirectarguments.md) structure.
- `indirectBufferOffset`: An integer that represents the location, in bytes, from the start of `indirectBuffer` where the indirect arguments structure begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

## See Also

- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:))*