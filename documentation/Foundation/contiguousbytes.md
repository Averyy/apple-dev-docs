# ContiguousBytes

**Framework**: Foundation  
**Kind**: protocol

A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol ContiguousBytes
```

## Topics

### Accessing Underlying Storage
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](contiguousbytes/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the type’s contiguous storage.

## Relationships

### Conforming Types
- [Data](data.md)

## See Also

- [struct Data](data.md)
  A byte buffer in memory.
- [protocol DataProtocol](dataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [protocol MutableDataProtocol](mutabledataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/contiguousbytes)*