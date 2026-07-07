# FullyInhabited

**Framework**: Swift  
**Kind**: typealias

A protocol for types whose memory can safely be written as or read from raw bytes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias FullyInhabited = ConvertibleFromBytes & ConvertibleToBytes
```

## See Also

- [protocol ConvertibleFromBytes](convertiblefrombytes.md)
  A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [protocol ConvertibleToBytes](convertibletobytes.md)
  A protocol for types whose memory can safely be read as individual raw bytes.
- [enum ByteOrder](byteorder.md)
  A byte ordering in memory.
- [func bitCast<T, U>(T, to: U.Type) -> U](bitcast(_:to:).md)
  Returns the bits of the given instance, interpreted as having the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fullyinhabited)*