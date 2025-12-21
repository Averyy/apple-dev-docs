# CMMutableDataBlockBuffer

**Framework**: Core Media  
**Kind**: struct

A block buffer that provides read-write access to a range of bytes.

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
struct CMMutableDataBlockBuffer
```

#### Overview

Mutable block buffer provides a contiguous range of data offsets (from 0 to [`count`](cmmutabledatablockbuffer/count.md)) a possibly non-contiguous range of bytes. The bytes referenced by this buffer are mutable.

## Topics

### Classes
- [CMMutableDataBlockBuffer.MemoryPool](cmmutabledatablockbuffer/memorypool.md)
  Optimize memory allocations when working with large block buffers.
### Structures
- [CMMutableDataBlockBuffer.BlockRegion](cmmutabledatablockbuffer/blockregion.md)
  A contiguous region of mutable memory within a block buffer.
- [CMMutableDataBlockBuffer.BlockSource](cmmutabledatablockbuffer/blocksource.md)
  Provides ability to allocate memory for blocks using custom allocator
### Operators
- [static func += (inout CMMutableDataBlockBuffer, consuming CMMutableDataBlockBuffer)](cmmutabledatablockbuffer/+=(_:_:).md)
  Appends the bytes of another block buffer without copying.
### Initializers
- [init(copying: UnsafePointer<AudioBufferList>, blockSource: CMMutableDataBlockBuffer.BlockSource?)](cmmutabledatablockbuffer/init(copying:blocksource:).md)
  Creates a block buffer by copying the given audio buffer list.
- [init(count: Int, blockSource: CMMutableDataBlockBuffer.BlockSource?)](cmmutabledatablockbuffer/init(count:blocksource:).md)
  Creates a block buffer with `count` number of bytes.
- [init(subBlockCapacity: Int, blockSource: CMMutableDataBlockBuffer.BlockSource?)](cmmutabledatablockbuffer/init(subblockcapacity:blocksource:).md)
  Creates a block buffer with at least `subBlockCapacity` number of sub blocks.
- [init(unsafeBlockBuffer: sending CMBlockBuffer)](cmmutabledatablockbuffer/init(unsafeblockbuffer:).md)
  Creates a mutable block buffer from an existing block buffer.
### Instance Properties
- [var count: Int](cmmutabledatablockbuffer/count.md)
  The number of bytes in the block buffer.
- [var endIndex: Int](cmmutabledatablockbuffer/endindex.md)
  The position one greater than the last valid subscript argument.
- [var indices: CMMutableDataBlockBuffer.Indices](cmmutabledatablockbuffer/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var isContiguous: Bool](cmmutabledatablockbuffer/iscontiguous.md)
  Determine whether the block buffer is contiguous.
- [var isEmpty: Bool](cmmutabledatablockbuffer/isempty.md)
  Indicates whether the block buffer is empty.
- [var startIndex: Int](cmmutabledatablockbuffer/startindex.md)
  The position of the first element.
### Instance Methods
- [func append(referenceOf: consuming CMMutableDataBlockBuffer, range: Range<Int>?, optimizeDepth: Bool)](cmmutabledatablockbuffer/append(referenceof:range:optimizedepth:).md)
  Append a reference to a range of another block buffer.
- [func copyBytes(to: UnsafeMutableRawBufferPointer)](cmmutabledatablockbuffer/copybytes(to:).md)
  Copy all bytes to the destination buffer.
- [func copyBytes<R>(to: UnsafeMutableRawBufferPointer, from: R)](cmmutabledatablockbuffer/copybytes(to:from:).md)
  Copy the bytes from the given range to the destination buffer.
- [func extend(by: Int)](cmmutabledatablockbuffer/extend(by:).md)
  Extend block buffer by appending a memory block of count bytes.
- [func isRangeContiguous(Range<Int>) -> Bool](cmmutabledatablockbuffer/israngecontiguous(_:).md)
  Returns true if the given range refers to a contiguous block of memory.
- [func replaceAll(repeating: UInt8)](cmmutabledatablockbuffer/replaceall(repeating:).md)
  Replace all bytes in the buffer with the given byte.
- [func replaceAll(with: UnsafeRawBufferPointer)](cmmutabledatablockbuffer/replaceall(with:)-4sg07.md)
  Replace all data in the buffer with new bytes.
- [func replaceAll(with: some DataProtocol)](cmmutabledatablockbuffer/replaceall(with:)-6jidg.md)
  Replace all data in the buffer with new bytes.
- [func replaceSubrange(Range<Int>, repeating: UInt8)](cmmutabledatablockbuffer/replacesubrange(_:repeating:).md)
  Fill a range in the buffer with given byte.
- [func replaceSubrange(Range<Int>, with: some DataProtocol)](cmmutabledatablockbuffer/replacesubrange(_:with:)-5w62q.md)
  Replace a range of bytes in the block buffer.
- [func replaceSubrange(Range<Int>, with: UnsafeRawBufferPointer)](cmmutabledatablockbuffer/replacesubrange(_:with:)-7rqdy.md)
  Replace a range of bytes in the block buffer.
- [func withContiguousMutableStorageIfAvailable<R>(in: Range<Int>?, (UnsafeMutableRawBufferPointer) throws -> sending R) rethrows -> sending R?](cmmutabledatablockbuffer/withcontiguousmutablestorageifavailable(in:_:).md)
  Access contents of the buffer if available as contiguous memory block.
- [func withContiguousStorageIfAvailable<R>(in: Range<Int>?, (UnsafeRawBufferPointer) throws -> sending R) rethrows -> sending R?](cmmutabledatablockbuffer/withcontiguousstorageifavailable(in:_:).md)
  Access contents of the buffer if available as contiguous memory block.
- [func withUnsafeBlockBuffer<R>((CMBlockBuffer) throws -> sending R) rethrows -> sending R](cmmutabledatablockbuffer/withunsafeblockbuffer(_:).md)
  Access the underlying CMBlockBuffer instance.
- [func withUnsafeBlockRegions<R>(([CMReadOnlyDataBlockBuffer.BlockRegion]) throws -> sending R) rethrows -> sending R](cmmutabledatablockbuffer/withunsafeblockregions(_:).md)
  Access the potentially non-contiguous memory region referenced by this block buffer.
- [func withUnsafeMutableBlockRegions<R>(([CMMutableDataBlockBuffer.BlockRegion]) throws -> sending R) rethrows -> sending R](cmmutabledatablockbuffer/withunsafemutableblockregions(_:).md)
  Access the potentially non-contiguous memory region referenced by this block buffer.
### Subscripts
- [subscript(Int) -> UInt8](cmmutabledatablockbuffer/subscript(_:).md)
  Accesses the data byte at the specified position.
### Type Aliases
- [CMMutableDataBlockBuffer.Index](cmmutabledatablockbuffer/index.md)
- [CMMutableDataBlockBuffer.Indices](cmmutabledatablockbuffer/indices-swift.typealias.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CMSampleBuffer](cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer](cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [CMTaggedBufferGroup](cmtaggedbuffergroup.md)
  Objective-C types and interfaces for working with Core Media tagged buffer groups.
- [CMFormatDescription](cmformatdescription-api.md)
  A media format descriptor that describes the samples in a sample buffer.
- [CMAttachment](cmattachment-api.md)
  Add supporting metadata to sample buffers.
- [struct CMTaggedBuffer](cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [struct CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
  A block buffer that provides read-only access to the a range of bytes.
- [struct CMReadySampleBuffer](cmreadysamplebuffer.md)
  Buffer carrying readily available samples of media data.
- [struct CMSampleDataReference](cmsampledatareference.md)
  References sample data in at a URL.
- [struct CMTaggedDynamicBuffer](cmtaggeddynamicbuffer.md)
  Contains a collection of tags associated with a read-only media buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer)*