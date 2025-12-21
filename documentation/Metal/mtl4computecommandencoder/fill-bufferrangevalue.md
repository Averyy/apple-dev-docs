# fill(buffer:range:value:)

**Framework**: Metal  
**Kind**: method

Encodes a command that fills a buffer with a constant value for each byte.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)
```

## Parameters

- `buffer`: A MTLBuffer instance the command assigns each byte in range to value.
- `range`: A range of bytes within the buffer the command assigns value to. The range’s count property needs to be greater than 0.
- `value`: The value to write to each byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/fill(buffer:range:value:))*