# CMBlockBuffer

**Framework**: Core Media  
**Kind**: class

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

## Topics

### Modifying a Block Buffer
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
- [func assureBlockMemory() throws](cmblockbuffer/assureblockmemory.md)
  Assures that the system allocates all memory blocks.
- [func withUnsafeMutableBytes<R>(atOffset: Int, (UnsafeMutableRawBufferPointer) throws -> R) throws -> R](cmblockbuffer/withunsafemutablebytes(atoffset:_:).md)
  Accesses the data that a block buffer represents.
### Inspecting a Block Buffer
- [var isEmpty: Bool](cmblockbuffer/isempty.md)
  A Boolean value that indicates whether the block buffer is empty.
### Accessing the Type Identifier
- [class var typeID: CFTypeID](cmblockbuffer/typeid.md)
  The type identifier for block buffer objects.
### Data Types
- [CMBlockBuffer.Error](cmblockbuffer/error.md)
  A structure that defines block buffer errors.
- [CMBlockBuffer.Flags](cmblockbuffer/flags.md)
  A structure that defines feature and control flags.
- [CMBlockBuffer.Slice](cmblockbuffer/slice.md)
  A slice of a `CMBlockBuffer` instance.
### Initializers
- [init(referencing: CMBlockBuffer)](cmblockbuffer/init(referencing:).md)
### Type Aliases
- [CMBlockBuffer.T](cmblockbuffer/t.md)

## Relationships

### Conforms To
- [CMAttachmentBearerProtocol](cmattachmentbearerprotocol.md)
- [CMBlockBufferProtocol](cmblockbufferprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol CMBlockBufferProtocol](cmblockbufferprotocol.md)
  A protocol for objects that operate on a range of a block buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer)*