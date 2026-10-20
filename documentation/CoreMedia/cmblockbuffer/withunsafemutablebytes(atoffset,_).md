# withUnsafeMutableBytes(atOffset:_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Accesses the data that a block buffer represents.

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
func withUnsafeMutableBytes<R>(atOffset offset: Int = 0, _ body: (UnsafeMutableRawBufferPointer) throws -> R) throws -> R
```

#### Return Value

The value, if any, that the body parameter returns

## Parameters

- `offset`: An offset within the buffer’s offset range.
- `body`: A closure the system calls with an [`UnsafeMutableRawBufferPointer`](../../Swift/unsafemutablerawbufferpointer.md) parameter that points to contiguous storage in the block buffer.

## See Also

### Modifying a Block Buffer
- [func append(length: Int, allocator: CFAllocator?, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](./append%28length,allocator,range,flags%29.md)
  Adds a memory block to an existing block buffer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer/withunsafemutablebytes(atoffset:_:))*