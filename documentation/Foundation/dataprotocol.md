# DataProtocol

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.

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
protocol DataProtocol : RandomAccessCollection where Self.Element == UInt8, Self.SubSequence : DataProtocol
```

## Topics

### Accessing Backing Storage
- [var regions: Self.Regions](./dataprotocol/regions-swift.property.md)
  A collection of buffers that make up the whole of the type conforming to a data protocol.
- [associatedtype Regions : BidirectionalCollection](./dataprotocol/regions-swift.associatedtype.md)
  A type that represents a collection of contiguous parts that make up the type conforming to a data protocol.
### Copying Underlying Bytes
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>) -> Int](./dataprotocol/copybytes%28to%29-52wps.md)
  Copies the bytes of data from the type into a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer) -> Int](./dataprotocol/copybytes%28to%29-3mk27.md)
  Copies the bytes of data from the type into a raw memory buffer.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, count: Int) -> Int](./dataprotocol/copybytes%28to,count%29-6krsm.md)
  Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) -> Int](./dataprotocol/copybytes%28to,count%29-29t5.md)
  Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [func copyBytes<DestinationType, R>(to: UnsafeMutableBufferPointer<DestinationType>, from: R) -> Int](./dataprotocol/copybytes%28to,from%29-1ol47.md)
  Copies a range of the bytes from the type into a typed memory buffer.
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R) -> Int](./dataprotocol/copybytes%28to,from%29-1y839.md)
  Copies a range of the bytes from the type into a raw memory buffer.
### Searching Within Data
- [func firstRange<D>(of: D) -> Range<Self.Index>?](./dataprotocol/firstrange%28of%29.md)
  Returns the first found range of the type’s data buffer.
- [func firstRange<D, R>(of: D, in: R) -> Range<Self.Index>?](./dataprotocol/firstrange%28of,in%29.md)
  Returns the first found range of the type’s data buffer.
- [func lastRange<D>(of: D) -> Range<Self.Index>?](./dataprotocol/lastrange%28of%29.md)
  Returns the last found range of the type’s data buffer.
- [func lastRange<D, R>(of: D, in: R) -> Range<Self.Index>?](./dataprotocol/lastrange%28of,in%29.md)
  Returns the last found range of the type’s data buffer.

## Relationships

### Inherits From
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sequence](../Swift/sequence.md)
### Inherited By
- [MutableDataProtocol](./mutabledataprotocol.md)
### Conforming Types
- [Data](./data.md)
- [NSData](./nsdata.md)
- [NSMutableData](./nsmutabledata.md)
- [NSPurgeableData](./nspurgeabledata.md)

## See Also

### Binary Data
- [struct Data](./data.md)
  A byte buffer in memory.
- [protocol MutableDataProtocol](./mutabledataprotocol.md)
  A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [protocol ContiguousBytes](./contiguousbytes.md)
  A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol)*