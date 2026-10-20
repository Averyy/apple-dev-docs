# CMBlockBufferProtocol

**Framework**: Core Media  
**Kind**: protocol  
**Role**: Protocol

A protocol for objects that operate on a range of a block buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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
- [func copyDataBytes(to: UnsafeMutableRawBufferPointer) throws](./cmblockbufferprotocol/copydatabytes%28to%29.md)
- [func dataBytes() throws -> Data](./cmblockbufferprotocol/databytes%28%29.md)
- [func fillDataBytes(with: UInt8) throws](./cmblockbufferprotocol/filldatabytes%28with%29.md)
- [func replaceDataBytes(with: UnsafeRawBufferPointer) throws](./cmblockbufferprotocol/replacedatabytes%28with%29.md)
- [var isContiguous: Bool](./cmblockbufferprotocol/iscontiguous.md)
- [func makeContiguous(allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](./cmblockbufferprotocol/makecontiguous%28allocator,deallocator,flags%29.md)
- [func makeContiguous(allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](./cmblockbufferprotocol/makecontiguous%28allocator,flags%29.md)
- [func withContiguousStorage<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](./cmblockbufferprotocol/withcontiguousstorage%28_%29.md)
### Inspecting a Block Buffer
- [var dataLength: Int](./cmblockbufferprotocol/datalength.md)
- [var startIndex: Int](./cmblockbufferprotocol/startindex.md)
- [var endIndex: Int](./cmblockbufferprotocol/endindex.md)
- [var owner: CMBlockBuffer](./cmblockbufferprotocol/owner.md)
### Subscripts
- [subscript(ClosedRange<Int>) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-7a30d.md)
  Creates a slice from a `ClosedRange`.
- [subscript(Range<Int>) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-1go3.md)
- [subscript(PartialRangeFrom<Int>) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-9ntfs.md)
- [subscript(PartialRangeUpTo<Int>) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-6ghj4.md)
- [subscript(PartialRangeThrough<Int>) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-532k5.md)
- [subscript(UnboundedRange) -> CMBlockBuffer.Slice](./cmblockbufferprotocol/subscript%28_%29-8jilq.md)

## Relationships

### Conforming Types
- [CMBlockBuffer](./cmblockbuffer.md)
- [CMBlockBuffer.Slice](./cmblockbuffer/slice.md)

## See Also

### Data Types
- [class CMBlockBuffer](./cmblockbuffer.md)
  A reference to a block buffer instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferprotocol)*