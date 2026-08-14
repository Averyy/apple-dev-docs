# MutableDataProtocol

**Framework**: Foundation  
**Kind**: protocol

A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.

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
protocol MutableDataProtocol : DataProtocol, MutableCollection, RangeReplaceableCollection
```

## Topics

### Resetting Backing Storage
- [func resetBytes<R>(in: R)](mutabledataprotocol/resetbytes(in:).md)
  Replaces the contents of the data buffer with zeros for the provided range.

## Relationships

### Inherits From
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [DataProtocol](dataprotocol.md)
- [MutableCollection](../swift/mutablecollection.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [RangeReplaceableCollection](../swift/rangereplaceablecollection.md)
- [Sequence](../swift/sequence.md)
### Conforming Types
- [Data](data.md)

## See Also

- [struct Data](data.md)
  A byte buffer in memory.
- [protocol DataProtocol](dataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [protocol ContiguousBytes](contiguousbytes.md)
  A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/mutabledataprotocol)*