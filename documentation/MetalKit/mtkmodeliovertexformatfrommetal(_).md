# MTKModelIOVertexFormatFromMetal(_:)

**Framework**: MetalKit  
**Kind**: func  
**Role**: Function

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

```c
extern MDLVertexFormat MTKModelIOVertexFormatFromMetal(MTLVertexFormat vertexFormat);
```

## Return Value

A Model I/O vertex format value.

## Discussion

This function returns [`MDLVertexFormat.invalid`](../ModelIO/mdlvertexformat/invalid.md) if no matching [`MDLVertexFormat`](../ModelIO/mdlvertexformat.md) exists.

## Parameters

- `vertexFormat`: A Metal vertex format to convert from.

## See Also

### Converting Between Model I/O and Metal Vertex Formats
- [func MTKMetalVertexFormatFromModelIO(MDLVertexFormat) -> MTLVertexFormat](./mtkmetalvertexformatfrommodelio%28_%29.md)
  Returns a converted Metal vertex format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmodeliovertexformatfrommetal(_:))*