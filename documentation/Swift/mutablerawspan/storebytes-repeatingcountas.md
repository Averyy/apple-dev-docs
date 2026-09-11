# storeBytes(repeating:count:as:_:)

**Framework**: Swift  
**Kind**: method

Stores the given value’s bytes repeatedly into this span’s memory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func storeBytes<T>(repeating repeatedValue: T, count: Int, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

#### Discussion

There must be at least `count * MemoryLayout<T>.stride` bytes available in the span.

## Parameters

- `repeatedValue`: The value to store as raw bytes.
- `count`: The number of copies of `repeatedValue` to store into this span.
- `type`: The type of the instance to store repeatedly.
- `byteOrder`: The order in which the bytes will be encoded to the span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(repeating:count:as:_:))*