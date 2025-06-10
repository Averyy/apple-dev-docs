# drawPrimitives(primitiveType:indirectBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a draw command that renders multiple instances of a geometric primitive with indirect arguments.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawPrimitives(primitiveType: MTLPrimitiveType, indirectBuffer: UInt64)
```

#### Discussion

When you use this function, Metal reads the parameters to the draw command from an [`MTLBuffer`](mtlbuffer.md) instance, allowing you to implement a GPU-driven workflow where a compute pipeline state determines the draw arguments.

You are responsible for ensuring that the address of the indirect buffer you provide to this method has 4-byte alignment.

Because this is a non-indexed draw call, Metal interprets the contents of the indirect buffer to match the layout of struct [`MTLDrawPrimitivesIndirectArguments`](mtldrawprimitivesindirectarguments.md).

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the indirect buffer that the `indirectBuffer` parameter references.

## Parameters

- `primitiveType`: A   representing how the command interprets vertex argument data.
- `indirectBuffer`: GPUAddress of a   instance with data that matches the layout of the    structure. You are responsible for ensuring that the   alignment of this address is 4 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/drawprimitives(primitivetype:indirectbuffer:))*