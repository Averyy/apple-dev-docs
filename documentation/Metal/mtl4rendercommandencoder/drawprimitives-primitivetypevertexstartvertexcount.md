# drawPrimitives(primitiveType:vertexStart:vertexCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders an instance of a geometric primitive.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)
```

#### Discussion

This command assigns each vertex a unique `vertex_id` value that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`.

Your vertex shader function can use this value to uniquely identify each vertex.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `vertexStart`: The lowest value the command passes to your vertex shader function’s parameter with the    attribute.
- `vertexCount`: An integer that represents the number of vertices of   the command draws.

## See Also

- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:))*