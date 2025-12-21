# drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)
```

#### Discussion

The command assigns each vertex a unique `vertex_id` value within its drawing instance that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`.

Additionally, the command assigns each drawing instance a unique `instance_id` value that increases from `0` through `(instanceCount - 1)`.

Your vertex shader can use the `vertex_id` value to uniquely identify each vertex in each drawing instance, and the `instance_id` value to identify which instance that vertex belongs to.

## Parameters

- `primitiveType`: A   represents how the command interprets vertex argument data.
- `vertexStart`: The lowest value the command passes to your vertex shader function’s parameter with   the   attribute.
- `vertexCount`: An integer that represents the number of vertices of   the command draws.
- `instanceCount`: An integer that represents the number of times the command draws   primitives   with   vertices.

## See Also

- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:))*