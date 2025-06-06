# assureBlockMemory()

**Framework**: Core Media  
**Kind**: method

Assures that the system allocates all memory blocks.

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
func assureBlockMemory() throws
```

## See Also

- [func append(length: Int, allocator: CFAllocator?, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(length:allocator:range:flags:).md)
  Adds a memory block to an existing block buffer.
- [func append(buffer: UnsafeMutableRawBufferPointer, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(buffer:allocator:flags:)-28keu.md)
  Adds a memory block to a block buffer using a custom allocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(buffer:allocator:flags:)-8fws8.md)
  Adds a sliced memory block to a block buffer using a custom allocator.
- [func append(length: Int, allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(length:allocator:deallocator:range:flags:).md)
  Adds a memory block to a block buffer using a custom allocator and deallocator.
- [func append(buffer: UnsafeMutableRawBufferPointer, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(buffer:deallocator:flags:)-3bfef.md)
  Adds a memory block to a block buffer with a custom deallocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(buffer:deallocator:flags:)-1ibzz.md)
  Adds a sliced memory block to a block buffer with a custom deallocator.
- [CMBlockBuffer.CustomBlockAllocator](cmblockbuffer/customblockallocator.md)
  A type that allocates memory blocks.
- [CMBlockBuffer.CustomBlockDeallocator](cmblockbuffer/customblockdeallocator.md)
  A type that deallocates memory blocks.
- [func append<T>(bufferReference: T, flags: CMBlockBuffer.Flags) throws](cmblockbuffer/append(bufferreference:flags:).md)
  Adds a reference to another block buffer.
- [func withUnsafeMutableBytes<R>(atOffset: Int, (UnsafeMutableRawBufferPointer) throws -> R) throws -> R](cmblockbuffer/withunsafemutablebytes(atoffset:_:).md)
  Accesses the data that a block buffer represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer/assureblockmemory())*