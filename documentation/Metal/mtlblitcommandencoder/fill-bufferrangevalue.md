# fill(buffer:range:value:)

**Framework**: Metal  
**Kind**: method

Encodes a command that fills a buffer with a constant value for each byte.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)
```

## Parameters

- `buffer`: A buffer instance the command assigns each byte in   to  .
- `range`: A range of bytes within the   the command assigns   to. The range’s   property needs to be greater than  . The range’s  ,  , and   properties need to be a multiple of   in macOS, but can be any value in iOS and tvOS.
- `value`: The value to write to each byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/fill(buffer:range:value:))*