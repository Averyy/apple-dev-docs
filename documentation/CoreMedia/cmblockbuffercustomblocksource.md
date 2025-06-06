# CMBlockBufferCustomBlockSource

**Framework**: Core Media  
**Kind**: struct

A structure to support custom memory allocation and deallocation for a block used in a block buffer.

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
struct CMBlockBufferCustomBlockSource
```

#### Overview

This structure allows a client to provide a custom facility for obtaining the memory block to be used in a `CMBlockBuffer`. You use this structure with functions that accept a memory block allocator.

## Topics

### Initializers
- [init()](cmblockbuffercustomblocksource/init.md)
- [init(version: UInt32, AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?, FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?, refCon: UnsafeMutableRawPointer?)](cmblockbuffercustomblocksource/init(version:allocateblock:freeblock:refcon:).md)
### Properties
- [var AllocateBlock: ((UnsafeMutableRawPointer?, Int) -> UnsafeMutableRawPointer?)?](cmblockbuffercustomblocksource/allocateblock.md)
  The function to allocate memory.
- [var FreeBlock: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Void)?](cmblockbuffercustomblocksource/freeblock.md)
  A function to call once when the `CMBlockBuffer` is disposed.
- [var refCon: UnsafeMutableRawPointer?](cmblockbuffercustomblocksource/refcon.md)
  Contextual information passed to both the allocate and free function calls.
- [var version: UInt32](cmblockbuffercustomblocksource/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreateempty(allocator:capacity:flags:blockbufferout:).md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithMemoryBlock(allocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that’s backed by a memory block.
- [func CMBlockBufferCreateWithBufferReference(allocator: CFAllocator?, referenceBuffer: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithbufferreference(allocator:referencebuffer:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that refers to another block buffer object.
- [func CMBlockBufferCreateContiguous(allocator: CFAllocator?, sourceBuffer: CMBlockBuffer, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatecontiguous(allocator:sourcebuffer:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that contains a contiguous copy of, or reference to, the data specified by the parameters.
- [typealias CMBlockBufferFlags](cmblockbufferflags.md)
  A type for flags that control behaviors and features of block buffer APIs.
- [Block Buffer Flags](block-buffer-flags.md)
  An enumeration of flags that control behaviors and features of block buffer APIs.
- [Custom Block Source Version](custom-block-source-version.md)
  A custom block source version identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource)*