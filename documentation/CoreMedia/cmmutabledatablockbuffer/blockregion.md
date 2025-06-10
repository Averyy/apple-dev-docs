# CMMutableDataBlockBuffer.BlockRegion

**Framework**: Core Media  
**Kind**: struct

A contiguous region of mutable memory within a block buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct BlockRegion
```

## Topics

### Instance Properties
- [var count: Int](cmmutabledatablockbuffer/blockregion/count.md)
  Number of bytes in the block region
- [var endIndex: Int](cmmutabledatablockbuffer/blockregion/endindex.md)
  The position one greater than the last valid subscript argument.
- [var regions: CollectionOfOne<CMMutableDataBlockBuffer.BlockRegion>](cmmutabledatablockbuffer/blockregion/regions.md)
  The single buffer that makes up this region.
- [let startIndex: Int](cmmutabledatablockbuffer/blockregion/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func withUnsafeBytes<ResultType>((UnsafeRawBufferPointer) throws -> ResultType) rethrows -> ResultType](cmmutabledatablockbuffer/blockregion/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the region’s contiguous storage.
- [func withUnsafeMutableBytes<ResultType>((UnsafeMutableRawBufferPointer) throws -> ResultType) rethrows -> ResultType](cmmutabledatablockbuffer/blockregion/withunsafemutablebytes(_:).md)
  Calls the given closure with a mutable pointer to the underlying bytes of the region’s contiguous storage.
### Subscripts
- [subscript(CMMutableDataBlockBuffer.BlockRegion.Index) -> UInt8](cmmutabledatablockbuffer/blockregion/subscript(_:).md)
  Accesses the data byte at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [DataProtocol](../Foundation/DataProtocol.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blockregion)*