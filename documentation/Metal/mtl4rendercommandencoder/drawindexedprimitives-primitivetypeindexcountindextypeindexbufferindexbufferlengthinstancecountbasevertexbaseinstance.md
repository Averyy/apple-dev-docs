# drawIndexedPrimitives(primitiveType:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices, starting with a custom vertex and instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)
```

#### Discussion

Use this method to perform instanced indexed drawing, where an index buffer determines how Metal assembles primitives whilst customizing the base vertex and base instance value Metal passes to the vertex shader function.

The command assigns each drawing instance a unique `instance_id` value that increases from `baseInstance` through `(baseInstance + instanceCount - 1)`. Your shader can use this value to identify which instance the vertex belongs to.

Metal imposes some restrictions on the index buffer’s address, which needs to be 2- or 4-byte aligned, and its length in bytes, which needs to be a multiple of 2 or 4, depending on whether the format of the index is [`MTLIndexType.uint16`](mtlindextype/uint16.md) or [`MTLIndexType.uint32`](mtlindextype/uint32.md).

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the index buffer the `indexBuffer` parameter references.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `indexCount`: An integer that represents the number of vertices the command reads from  .
- `indexType`: A   instance that represents the index format.
- `indexBuffer`: GPUAddress of a   instance that contains   indices of   format.   You are responsible for ensuring this address is aligned to 2 bytes if the   format is   , and aligned to 4 bytes if the format is   .
- `indexBufferLength`: An integer that represents the length of  , in bytes. You are responsible for   ensuring this this size is a multiple of 2 if the   format is  ,   and a multiple of 4 if the format is  .   If this draw call causes Metal to read indices at or beyond the  , Metal   continues to execute them assigning a value of   to the   attribute.
- `instanceCount`: An integer that represents the number of times the command draws   with    vertices.
- `baseVertex`: The lowest value the command passes to your vertex shader functions’s parameter with the    attribute. Metal disregards this value and assigns   to the   attribute for all   primitives that require loading indices at a byte offset of   or greater.
- `baseInstance`: The lowest value the command passes to your vertex shader’s parameter with the   attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indexcount:indextype:indexbuffer:indexbufferlength:instancecount:basevertex:baseinstance:))*