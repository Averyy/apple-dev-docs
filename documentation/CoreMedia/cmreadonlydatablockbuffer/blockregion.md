# CMReadOnlyDataBlockBuffer.BlockRegion

**Framework**: Core Media  
**Kind**: struct

A contiguous region of memory within a block buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
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
- [var count: Int](cmreadonlydatablockbuffer/blockregion/count.md)
  Number of bytes in the block region
- [var endIndex: Int](cmreadonlydatablockbuffer/blockregion/endindex.md)
  The position one greater than the last valid subscript argument.
- [var regions: CollectionOfOne<CMReadOnlyDataBlockBuffer.BlockRegion>](cmreadonlydatablockbuffer/blockregion/regions.md)
  The single buffer that makes up this region.
- [let startIndex: Int](cmreadonlydatablockbuffer/blockregion/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R?](cmreadonlydatablockbuffer/blockregion/withcontiguousstorageifavailable(_:).md)
  Access contents of the buffer if available as contiguous memory block.
- [func withUnsafeBytes<ResultType>((UnsafeRawBufferPointer) throws -> ResultType) rethrows -> ResultType](cmreadonlydatablockbuffer/blockregion/withunsafebytes(_:).md)
  Calls the given closure with a pointer to the underlying bytes of the region’s contiguous storage.
### Subscripts
- [subscript(CMReadOnlyDataBlockBuffer.BlockRegion.Index) -> UInt8](cmreadonlydatablockbuffer/blockregion/subscript(_:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/blockregion)*