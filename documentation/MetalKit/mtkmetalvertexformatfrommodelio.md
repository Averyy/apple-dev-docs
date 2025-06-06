# MTKMetalVertexFormatFromModelIO(_:)

**Framework**: MetalKit  
**Kind**: func

Returns a converted Metal vertex format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTKMetalVertexFormatFromModelIO(_ vertexFormat: MDLVertexFormat) -> MTLVertexFormat
```

#### Return Value

A Metal vertex format value.

#### Discussion

This function returns [`MTLVertexFormat.invalid`](https://developer.apple.com/documentation/Metal/MTLVertexFormat/invalid) if no matching [`MTLVertexFormat`](https://developer.apple.com/documentation/Metal/MTLVertexFormat) exists.

## Parameters

- `vertexFormat`: A Model I/O vertex format to convert from.

## See Also

- [func MTKModelIOVertexFormatFromMetal(MTLVertexFormat) -> MDLVertexFormat](mtkmodeliovertexformatfrommetal(_:).md)
  Returns a converted Model I/O vertex format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmetalvertexformatfrommodelio(_:))*