# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a vertex format from a raw integer value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(rawValue: UInt)
```

#### Discussion

Use the [`MTLVertexFormat`](mtlvertexformat.md) structure’s type properties, such as [`MTLVertexFormat.uchar4Normalized_bgra`](mtlvertexformat/uchar4normalized_bgra.md), instead of this initializer.

## Parameters

- `rawValue`: The underlying integer value that represents a vertex format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexformat/init(rawvalue:))*