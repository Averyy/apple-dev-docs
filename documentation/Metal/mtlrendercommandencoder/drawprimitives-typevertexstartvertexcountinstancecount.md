# drawPrimitives(type:vertexStart:vertexCount:instanceCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)
```

#### Discussion

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [`MTLCommandBuffer`](mtlcommandbuffer.md).

## Parameters

- `primitiveType`: See the   method and its siblings for more information about setting an entry in the vertex shader argument table for buffers.
- `vertexStart`: For more information about the   argument attribute for vertex shaders, see the  .
- `vertexCount`: An integer that represents the number of vertices of   the command draws per instance.
- `instanceCount`: For more information about the   argument attribute for vertex shaders, the  .

## See Also

- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive that starts with a custom instance identification number.
- [func drawPrimitives(type: MTLPrimitiveType, indirectBuffer: any MTLBuffer, indirectBufferOffset: Int)](mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/drawprimitives(type:vertexstart:vertexcount:instancecount:))*