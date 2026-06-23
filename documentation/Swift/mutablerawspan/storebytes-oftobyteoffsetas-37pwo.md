# storeBytes(of:toByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Stores the given value’s bytes into the span’s raw memory at the specified byte offset.

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
mutating func storeBytes<T>(of value: T, toByteOffset offset: Int = 0, as type: T.Type) where T : BitwiseCopyable
```

## Parameters

- `value`: The value to store as raw bytes.
- `offset`: The offset from the start of the span, in bytes. `offset` must be nonnegative. The default is zero.
- `type`: The type of `value`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:)-37pwo)*