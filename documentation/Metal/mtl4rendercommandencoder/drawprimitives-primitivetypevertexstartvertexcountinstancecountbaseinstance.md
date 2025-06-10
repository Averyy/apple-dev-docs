# drawPrimitives(primitiveType:vertexStart:vertexCount:instanceCount:baseInstance:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)
```

#### Discussion

The command assigns each vertex a unique `vertex_id` value within its drawing instance that increases from `vertexStart` through `(vertexStart + vertexCount - 1)`.

Additionally, the command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`.

Your vertex shader can use the `vertex_id` value to uniquely identify each vertex in each drawing instance, and the `instance_id` value to identify which instance that vertex belongs to.

## Parameters

- `primitiveType`: A    representing how the command interprets vertex argument data.
- `vertexStart`: The lowest value the command passes to your vertex shader function’s parameter with   the   attribute.
- `vertexCount`: An integer that represents the number of vertices of   the command draws.
- `instanceCount`: An integer that represents the number of times the command draws    with   vertices.
- `baseInstance`: The lowest value the command passes to your vertex shader function’s parameter with   the   attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:))*