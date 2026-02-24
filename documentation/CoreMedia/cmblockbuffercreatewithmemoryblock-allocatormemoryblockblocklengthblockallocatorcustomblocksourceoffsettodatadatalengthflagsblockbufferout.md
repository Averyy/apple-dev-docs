# CMBlockBufferCreateWithMemoryBlock(allocator:memoryBlock:blockLength:blockAllocator:customBlockSource:offsetToData:dataLength:flags:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a block buffer that’s backed by a memory block.

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
func CMBlockBufferCreateWithMemoryBlock(allocator structureAllocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Creates a new `CMBlockBuffer` backed by a memory block. The memory block may be statically allocated, dynamically allocated using the given allocator (or `customBlockSource`) or not yet allocated. The returned `CMBlockBuffer` may be further expanded using `CMBlockBufferAppendMemoryBlock` and/or `CMBlockBufferAppendBufferReference`.

## Parameters

- `structureAllocator`: Allocator to use for allocating the `CMBlockBuffer` object. Pass `NULL` to use the default allocator.
- `memoryBlock`: Block of memory to hold buffered data. If `NULL`, a memory block will be allocated when needed (via a call to `CMBlockBufferAssureBlockMemory` using the provided `blockAllocator` or `customBlockSource`. If non-`NULL`, the block will be used and will be deallocated when the new `CMBlockBuffer` is finalized (i.e. released for the last time).
- `blockLength`: Overall length of the memory block in bytes. Must not be zero. This is the size of the supplied memory block or the size to allocate if `memoryBlock` is `NULL`.
- `blockAllocator`: Allocator to be used for allocating the `memoryBlock`, if `memoryBlock` is `NULL`. If `memoryBlock` is non-`NULL`, this allocator will be used to deallocate it if provided. Passing `NULL` will cause the default allocator (as set at the time of the call) to be used. Pass `kCFAllocatorNull` if no deallocation is desired.
- `customBlockSource`: If non-`NULL`, it will be used for the allocation and freeing of the memory block (the `blockAllocator` parameter is ignored). If provided, and the `memoryBlock` parameter is `NULL`, its `AllocateBlock()` routine must be non-NULL. Allocate will be called once, if successful, when the `memoryBlock` is allocated. `FreeBlock()` will be called once when the `CMBlockBuffer` is disposed.
- `offsetToData`: Offset within the `memoryBlock` at which the `CMBlockBuffer` should refer to data.
- `dataLength`: Number of relevant data bytes, starting at `offsetToData`, within the memory block.
- `flags`: Feature and control flags.
- `blockBufferOut`: Receives newly-created `CMBlockBuffer` object with a retain count of 1. Must not be `NULL`.

## See Also

- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreateempty(allocator:capacity:flags:blockbufferout:).md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithBufferReference(allocator: CFAllocator?, referenceBuffer: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithbufferreference(allocator:referencebuffer:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that refers to another block buffer object.
- [func CMBlockBufferCreateContiguous(allocator: CFAllocator?, sourceBuffer: CMBlockBuffer, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatecontiguous(allocator:sourcebuffer:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that contains a contiguous copy of, or reference to, the data specified by the parameters.
- [typealias CMBlockBufferFlags](cmblockbufferflags.md)
  A type for flags that control behaviors and features of block buffer APIs.
- [Block Buffer Flags](block-buffer-flags.md)
  An enumeration of flags that control behaviors and features of block buffer APIs.
- [struct CMBlockBufferCustomBlockSource](cmblockbuffercustomblocksource.md)
  A structure to support custom memory allocation and deallocation for a block used in a block buffer.
- [Custom Block Source Version](custom-block-source-version.md)
  A custom block source version identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:))*