# storeBytes(repeating:count:as:)

**Framework**: Swift  
**Kind**: method

Stores the given value’s bytes repeatedly into this span’s memory.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
mutating func storeBytes<T>(repeating repeatedValue: T, count: Int, as type: T.Type) where T : BitwiseCopyable, T : ConvertibleToBytes
```

#### Discussion

There must be at least `count * MemoryLayout<T>.stride` bytes available in the span.

## Parameters

- `repeatedValue`: The value to store as raw bytes.
- `count`: The number of copies of `repeatedValue` to store into this span.
- `type`: The type of the instance to store repeatedly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(repeating:count:as:)-7cd7p)*