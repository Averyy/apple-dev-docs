# MTKMetalVertexFormatFromModelIO(_:)

**Framework**: MetalKit  
**Kind**: func  
**Role**: Function

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

```c
extern MTLVertexFormat MTKMetalVertexFormatFromModelIO(MDLVertexFormat vertexFormat);
```

#### Return Value

A Metal vertex format value.

#### Discussion

This function returns [`MTLVertexFormat.invalid`](../Metal/mtlvertexformat/invalid.md) if no matching [`MTLVertexFormat`](../Metal/mtlvertexformat.md) exists.

## Parameters

- `vertexFormat`: A Model I/O vertex format to convert from.

## See Also

### Converting Between Model I/O and Metal Vertex Formats
- [func MTKModelIOVertexFormatFromMetal(MTLVertexFormat) -> MDLVertexFormat](./mtkmodeliovertexformatfrommetal%28_%29.md)
  Returns a converted Model I/O vertex format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmetalvertexformatfrommodelio(_:))*