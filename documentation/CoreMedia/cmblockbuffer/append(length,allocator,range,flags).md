# append(length:allocator:range:flags:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Adds a memory block to an existing block buffer.

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
func append(length: Int, allocator: CFAllocator? = kCFAllocatorDefault, range: Range<Int>? = nil, flags: CMBlockBuffer.Flags = []) throws
```

## Parameters

- `length`: The length of the memory block in bytes. Must not be zero. This is the size to allocate when you call the [`assureBlockMemory()`](./assureblockmemory%28%29.md) function.
- `allocator`: The allocator to use to allocate the memory block.
- `range`: The range within the memory block to which the block buffer should refer to data. If this value is `nil`, the block buffer uses the whole memory block.
- `flags`: Flags to control the behavior of the operation.

## See Also

### Modifying a Block Buffer
- [func append(buffer: UnsafeMutableRawBufferPointer, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](./append%28buffer,allocator,flags%29-28keu.md)
  Adds a memory block to a block buffer using a custom allocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](./append%28buffer,allocator,flags%29-8fws8.md)
  Adds a sliced memory block to a block buffer using a custom allocator.
- [func append(length: Int, allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](./append%28length,allocator,deallocator,range,flags%29.md)
  Adds a memory block to a block buffer using a custom allocator and deallocator.
- [func append(buffer: UnsafeMutableRawBufferPointer, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](./append%28buffer,deallocator,flags%29-3bfef.md)
  Adds a memory block to a block buffer with a custom deallocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](./append%28buffer,deallocator,flags%29-1ibzz.md)
  Adds a sliced memory block to a block buffer with a custom deallocator.
- [CMBlockBuffer.CustomBlockAllocator](./customblockallocator.md)
  A type that allocates memory blocks.
- [CMBlockBuffer.CustomBlockDeallocator](./customblockdeallocator.md)
  A type that deallocates memory blocks.
- [func append<T>(bufferReference: T, flags: CMBlockBuffer.Flags) throws](./append%28bufferreference,flags%29.md)
  Adds a reference to another block buffer.
- [func assureBlockMemory() throws](./assureblockmemory%28%29.md)
  Assures that the system allocates all memory blocks.
- [func withUnsafeMutableBytes<R>(atOffset: Int, (UnsafeMutableRawBufferPointer) throws -> R) throws -> R](./withunsafemutablebytes%28atoffset,_%29.md)
  Accesses the data that a block buffer represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer/append(length:allocator:range:flags:))*