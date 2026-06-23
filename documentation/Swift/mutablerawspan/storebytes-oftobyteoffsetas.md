# storeBytes(of:toByteOffset:as:_:)

**Framework**: Swift  
**Kind**: method

Stores the given value’s bytes to the specified offset into the span’s memory.

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
mutating func storeBytes<T>(of value: T, toByteOffset offset: Int, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

#### Discussion

The range of bytes required to store a value of type `T` starting at byte offset `offset` must be completely within the span. `offset` is not required to be aligned for `T`.

## Parameters

- `value`: The value to store as raw bytes.
- `offset`: The offset in bytes into the span’s memory at which to begin writing the bytes from the value.
- `type`: The type of the instance to store.
- `byteOrder`: The order in which the bytes will be encoded to the span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:_:))*