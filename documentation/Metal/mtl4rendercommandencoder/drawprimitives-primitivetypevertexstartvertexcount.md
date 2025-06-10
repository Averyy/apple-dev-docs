# drawPrimitives(primitiveType:vertexStart:vertexCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders an instance of a geometric primitive.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:))*