# MTKModelIOVertexFormatFromMetal(_:)

**Framework**: MetalKit  
**Kind**: func

Returns a converted Model I/O vertex format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTKModelIOVertexFormatFromMetal(_ vertexFormat: MTLVertexFormat) -> MDLVertexFormat
```

#### Return Value

A Model I/O vertex format value.

#### Discussion

This function returns [`MDLVertexFormat.invalid`](https://developer.apple.com/documentation/ModelIO/MDLVertexFormat/invalid) if no matching [`MDLVertexFormat`](https://developer.apple.com/documentation/ModelIO/MDLVertexFormat) exists.

## Parameters

- `vertexFormat`: A Metal vertex format to convert from.

## See Also

- [func MTKMetalVertexFormatFromModelIO(MDLVertexFormat) -> MTLVertexFormat](mtkmetalvertexformatfrommodelio(_:).md)
  Returns a converted Metal vertex format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmodeliovertexformatfrommetal(_:))*