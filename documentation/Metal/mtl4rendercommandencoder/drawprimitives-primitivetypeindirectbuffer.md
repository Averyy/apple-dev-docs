# drawPrimitives(primitiveType:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: MTLGPUAddress)
```

#### Discussion

When you use this function, Metal reads the parameters to the draw command from an [`MTLBuffer`](mtlbuffer.md) instance, allowing you to implement a GPU-driven workflow where a compute pipeline state determines the draw arguments.

You are responsible for ensuring that the address of the indirect buffer you provide to this method has 4-byte alignment.

Because this is a non-indexed draw call, Metal interprets the contents of the indirect buffer to match the layout of struct [`MTLDrawPrimitivesIndirectArguments`](mtldrawprimitivesindirectarguments.md).

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `indirectBuffer`: GPUAddress of a   instance with data that matches the layout of the    structure. You are responsible for ensuring that the   alignment of this address is 4 bytes.

## See Also

- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:).md)
  Encodes a draw command that renders an instance of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive.
- [func drawPrimitives(primitiveType: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](mtl4rendercommandencoder/drawprimitives(primitivetype:vertexstart:vertexcount:instancecount:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive, starting with a custom instance identification number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:))*