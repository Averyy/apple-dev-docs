# CMMutableDataBlockBuffer.BlockRegion

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A contiguous region of mutable memory within a block buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct BlockRegion
```

## Topics

### Instance Properties
- [var count: Int](./blockregion/count.md)
  Number of bytes in the block region
- [var endIndex: Int](./blockregion/endindex.md)
  The position one greater than the last valid subscript argument.
- [var regions: CollectionOfOne<CMMutableDataBlockBuffer.BlockRegion>](./blockregion/regions.md)
  The single buffer that makes up this region.
- [let startIndex: Int](./blockregion/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func withUnsafeBytes<ResultType>((UnsafeRawBufferPointer) throws -> ResultType) rethrows -> ResultType](./blockregion/withunsafebytes%28_%29.md)
  Calls the given closure with a pointer to the underlying bytes of the region’s contiguous storage.
- [func withUnsafeMutableBytes<ResultType>((UnsafeMutableRawBufferPointer) throws -> ResultType) rethrows -> ResultType](./blockregion/withunsafemutablebytes%28_%29.md)
  Calls the given closure with a mutable pointer to the underlying bytes of the region’s contiguous storage.
### Subscripts
- [subscript(CMMutableDataBlockBuffer.BlockRegion.Index) -> UInt8](./blockregion/subscript%28_%29.md)
  Accesses the data byte at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [ContiguousBytes](../../Foundation/contiguousbytes.md)
- [DataProtocol](../../Foundation/dataprotocol.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blockregion)*