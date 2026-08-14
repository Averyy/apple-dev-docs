# fill(buffer:range:value:)

**Framework**: Metal  
**Kind**: method

Encodes a command that fills a buffer with a constant value for each byte.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)
```

## Parameters

- `buffer`: A buffer instance the command assigns each byte in `range` to `value`.
- `range`: A range of bytes within the `buffer` the command assigns `value` to. The range’s [`count`](https://developer.apple.com/documentation/swift/collection/count) property needs to be greater than `0`. The range’s [`count`](https://developer.apple.com/documentation/swift/collection/count), [`lowerBound`](https://developer.apple.com/documentation/swift/range/lowerbound), and [`upperBound`](https://developer.apple.com/documentation/swift/range/upperbound) properties need to be a multiple of `4` in macOS, but can be any value in iOS and tvOS.
- `value`: The value to write to each byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/fill(buffer:range:value:))*