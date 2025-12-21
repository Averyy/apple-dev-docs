# drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders an instance of a geometric primitive with indexed vertices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int)
```

#### Discussion

Use this method to perform indexed drawing, where an index buffer determines how Metal assembles primitives.

Metal imposes some restrictions on the index buffer’s address, which needs to be 2- or 4-byte aligned, and its length in bytes, which needs to be a multiple of 2 or 4, depending on whether the format of the index is [`MTLIndexType.uint16`](mtlindextype/uint16.md) or [`MTLIndexType.uint32`](mtlindextype/uint32.md).

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the index buffer the `indexBuffer` parameter references.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `indexCount`: An integer that represents the number of vertices the command reads from  .
- `indexType`: A   instance that represents the index format.
- `indexBuffer`: GPUAddress of a   instance that contains   indices of   format.   You are responsible for ensuring this address is aligned to 2 bytes if the   format is   , and aligned to 4 bytes if the format is   .
- `indexBufferLength`: An integer that represents the length of  , in bytes. You are responsible for   ensuring this this size is a multiple of 2 if the   format is  ,   and a multiple of 4 if the format is  .   If this draw call causes Metal to read indices at or beyond the  , Metal   continues to execute them assigning a value of   to the   attribute.

## See Also

- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, instanceCount: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:basevertex:baseinstance:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.
- [func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: MTLGPUAddress, indexBufferLength: Int, indirectBuffer: MTLGPUAddress)](mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indextype:indexbuffer:indexbufferlength:indirectbuffer:).md)
  Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:))*