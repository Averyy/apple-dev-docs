# CMBlockBufferProtocol

**Framework**: Core Media  
**Kind**: protocol

A protocol for objects that operate on a range of a block buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol CMBlockBufferProtocol
```

## Topics

### Modifying a Block Buffer
- [func copyDataBytes(to: UnsafeMutableRawBufferPointer) throws](cmblockbufferprotocol/copydatabytes(to:).md)
- [func dataBytes() throws -> Data](cmblockbufferprotocol/databytes.md)
- [func fillDataBytes(with: UInt8) throws](cmblockbufferprotocol/filldatabytes(with:).md)
- [func replaceDataBytes(with: UnsafeRawBufferPointer) throws](cmblockbufferprotocol/replacedatabytes(with:).md)
- [var isContiguous: Bool](cmblockbufferprotocol/iscontiguous.md)
- [func makeContiguous(allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](cmblockbufferprotocol/makecontiguous(allocator:deallocator:flags:).md)
- [func makeContiguous(allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](cmblockbufferprotocol/makecontiguous(allocator:flags:).md)
- [func withContiguousStorage<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](cmblockbufferprotocol/withcontiguousstorage(_:).md)
### Inspecting a Block Buffer
- [var dataLength: Int](cmblockbufferprotocol/datalength.md)
- [var startIndex: Int](cmblockbufferprotocol/startindex.md)
- [var endIndex: Int](cmblockbufferprotocol/endindex.md)
- [var owner: CMBlockBuffer](cmblockbufferprotocol/owner.md)
### Subscripts
- [subscript(ClosedRange<Int>) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-7a30d.md)
  Creates a slice from a `ClosedRange`.
- [subscript(Range<Int>) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-1go3.md)
- [subscript(PartialRangeFrom<Int>) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-9ntfs.md)
- [subscript(PartialRangeUpTo<Int>) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-6ghj4.md)
- [subscript(PartialRangeThrough<Int>) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-532k5.md)
- [subscript((UnboundedRange_) -> ()) -> CMBlockBuffer.Slice](cmblockbufferprotocol/subscript(_:)-8jilq.md)

## Relationships

### Conforming Types
- [CMBlockBuffer](cmblockbuffer.md)
- [CMBlockBuffer.Slice](cmblockbuffer/slice.md)

## See Also

- [class CMBlockBuffer](cmblockbuffer.md)
  A reference to a block buffer instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferprotocol)*