# append(_:as:_:)

**Framework**: Swift  
**Kind**: method

Appends the given value’s bytes to this span’s bytes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func append<T>(_ value: T, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

#### Discussion

There must be at least `MemoryLayout<T>.size` bytes available in the span.

## Parameters

- `value`: The value to store as raw bytes.
- `type`: The type of the instance to store.
- `byteOrder`: The order in which the bytes will be encoded to the span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/append(_:as:_:))*