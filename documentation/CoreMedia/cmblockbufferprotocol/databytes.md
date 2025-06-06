# dataBytes()

**Framework**: Core Media  
**Kind**: method

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
func dataBytes() throws -> Data
```

## See Also

- [func copyDataBytes(to: UnsafeMutableRawBufferPointer) throws](cmblockbufferprotocol/copydatabytes(to:).md)
- [func fillDataBytes(with: UInt8) throws](cmblockbufferprotocol/filldatabytes(with:).md)
- [func replaceDataBytes(with: UnsafeRawBufferPointer) throws](cmblockbufferprotocol/replacedatabytes(with:).md)
- [var isContiguous: Bool](cmblockbufferprotocol/iscontiguous.md)
- [func makeContiguous(allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](cmblockbufferprotocol/makecontiguous(allocator:deallocator:flags:).md)
- [func makeContiguous(allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](cmblockbufferprotocol/makecontiguous(allocator:flags:).md)
- [func withContiguousStorage<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](cmblockbufferprotocol/withcontiguousstorage(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferprotocol/databytes())*