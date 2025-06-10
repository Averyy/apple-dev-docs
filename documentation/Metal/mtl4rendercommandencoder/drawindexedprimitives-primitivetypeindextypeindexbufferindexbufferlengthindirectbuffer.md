# drawIndexedPrimitives(primitiveType:indexType:indexBuffer:indexBufferLength:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indexed vertices and indirect arguments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawIndexedPrimitives(primitiveType: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: UInt64, indexBufferLength: Int, indirectBuffer: UInt64)
```

#### Discussion

When you use this function, Metal reads the parameters to the draw command from an [`MTLBuffer`](mtlbuffer.md) instance, allowing you to implement a GPU-driven workflow where a compute pipeline state determines the draw arguments.

Because this is an indexed draw call, Metal interprets the contents of the indirect buffer to match the layout of struct [`MTLDrawIndexedPrimitivesIndirectArguments`](mtldrawindexedprimitivesindirectarguments.md), which includes `indexStart` and `indexCount` members, denoting a range within the index buffer you provide in the `indexBuffer` parameter.

The range of indices within the `indexBuffer` form the primitives Metal draws.

Metal imposes some restrictions on the index buffer’s address, which needs to be 2- or 4-byte aligned, and its length in bytes, which needs to be a multiple of 2 or 4, depending on whether the format of the index is [`MTLIndexType.uint16`](mtlindextype/uint16.md) or [`MTLIndexType.uint32`](mtlindextype/uint32.md).

Similarly, you are responsible for ensuring the indirect buffer’s address has 4-byte alignment.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references, and of the index buffer the `indexBuffer` parameter references.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `indexType`: A   instance that represents the index format.
- `indexBuffer`: GPUAddress of a   instance that contains   indices of   format.   You are responsible for ensuring this address is aligned to 2 bytes if the   format is   , and aligned to 4 bytes if the format is   .
- `indexBufferLength`: An integer that represents the length of  , in bytes. You are responsible for   ensuring this this size is a multiple of 2 if the   format is  ,   and a multiple of 4 if the format is  .   If this draw call causes Metal to read indices at or beyond the  , Metal   continues to execute them assigning a value of   to the   attribute.
- `indirectBuffer`: GPUAddress of an   instance with data that matches the layout of the    structure. This address requires 4-byte alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawindexedprimitives(primitivetype:indextype:indexbuffer:indexbufferlength:indirectbuffer:))*