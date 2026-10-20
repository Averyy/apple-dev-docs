# copyDataBytes(to:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

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
func copyDataBytes(to destination: UnsafeMutableRawBufferPointer) throws
```

## See Also

### Modifying a Block Buffer
- [func dataBytes() throws -> Data](./databytes%28%29.md)
- [func fillDataBytes(with: UInt8) throws](./filldatabytes%28with%29.md)
- [func replaceDataBytes(with: UnsafeRawBufferPointer) throws](./replacedatabytes%28with%29.md)
- [var isContiguous: Bool](./iscontiguous.md)
- [func makeContiguous(allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](./makecontiguous%28allocator,deallocator,flags%29.md)
- [func makeContiguous(allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws -> CMBlockBuffer](./makecontiguous%28allocator,flags%29.md)
- [func withContiguousStorage<R>((UnsafeRawBufferPointer) throws -> R) throws -> R](./withcontiguousstorage%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferprotocol/copydatabytes(to:))*