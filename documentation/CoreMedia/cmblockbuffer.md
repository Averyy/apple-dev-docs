# CMBlockBuffer

**Framework**: Core Media  
**Kind**: class  
**Role**: Class

A reference to a block buffer instance.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CMBlockBuffer
```

```c
typedef struct OpaqueCMBlockBuffer * CMBlockBufferRef;
```

## Topics

### Modifying a Block Buffer
- [func append(length: Int, allocator: CFAllocator?, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28length,allocator,range,flags%29.md)
  Adds a memory block to an existing block buffer.
- [func append(buffer: UnsafeMutableRawBufferPointer, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28buffer,allocator,flags%29-28keu.md)
  Adds a memory block to a block buffer using a custom allocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, allocator: CFAllocator?, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28buffer,allocator,flags%29-8fws8.md)
  Adds a sliced memory block to a block buffer using a custom allocator.
- [func append(length: Int, allocator: CMBlockBuffer.CustomBlockAllocator, deallocator: CMBlockBuffer.CustomBlockDeallocator, range: Range<Int>?, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28length,allocator,deallocator,range,flags%29.md)
  Adds a memory block to a block buffer using a custom allocator and deallocator.
- [func append(buffer: UnsafeMutableRawBufferPointer, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28buffer,deallocator,flags%29-3bfef.md)
  Adds a memory block to a block buffer with a custom deallocator.
- [func append(buffer: Slice<UnsafeMutableRawBufferPointer>, deallocator: CMBlockBuffer.CustomBlockDeallocator, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28buffer,deallocator,flags%29-1ibzz.md)
  Adds a sliced memory block to a block buffer with a custom deallocator.
- [CMBlockBuffer.CustomBlockAllocator](./cmblockbuffer/customblockallocator.md)
  A type that allocates memory blocks.
- [CMBlockBuffer.CustomBlockDeallocator](./cmblockbuffer/customblockdeallocator.md)
  A type that deallocates memory blocks.
- [func append<T>(bufferReference: T, flags: CMBlockBuffer.Flags) throws](./cmblockbuffer/append%28bufferreference,flags%29.md)
  Adds a reference to another block buffer.
- [func assureBlockMemory() throws](./cmblockbuffer/assureblockmemory%28%29.md)
  Assures that the system allocates all memory blocks.
- [func withUnsafeMutableBytes<R>(atOffset: Int, (UnsafeMutableRawBufferPointer) throws -> R) throws -> R](./cmblockbuffer/withunsafemutablebytes%28atoffset,_%29.md)
  Accesses the data that a block buffer represents.
### Inspecting a Block Buffer
- [var isEmpty: Bool](./cmblockbuffer/isempty.md)
  A Boolean value that indicates whether the block buffer is empty.
### Accessing the Type Identifier
- [class var typeID: CFTypeID](./cmblockbuffer/typeid.md)
  The type identifier for block buffer objects.
### Data Types
- [CMBlockBuffer.Error](./cmblockbuffer/error.md)
  A structure that defines block buffer errors.
- [CMBlockBuffer.Flags](./cmblockbuffer/flags.md)
  A structure that defines feature and control flags.
- [CMBlockBuffer.Slice](./cmblockbuffer/slice.md)
  A slice of a `CMBlockBuffer` instance.
### Initializers
- [init(referencing: CMBlockBuffer)](./cmblockbuffer/init%28referencing%29.md)
### Type Aliases
- [CMBlockBuffer.T](./cmblockbuffer/t.md)

## Relationships

### Conforms To
- [CMAttachmentBearerProtocol](./cmattachmentbearerprotocol.md)
- [CMBlockBufferProtocol](./cmblockbufferprotocol.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Data Types
- [protocol CMBlockBufferProtocol](./cmblockbufferprotocol.md)
  A protocol for objects that operate on a range of a block buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer)*