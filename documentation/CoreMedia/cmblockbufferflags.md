# CMBlockBufferFlags

**Framework**: Core Media  
**Kind**: typealias

A type for flags that control behaviors and features of block buffer APIs.

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
typealias CMBlockBufferFlags = UInt32
```

## Topics

### Constants
- [var kCMBlockBufferAssureMemoryNowFlag: CMBlockBufferFlags](kcmblockbufferassurememorynowflag.md)
  When passed to routines that accept block allocators, causes the memory block to be allocated immediately.
- [var kCMBlockBufferAlwaysCopyDataFlag: CMBlockBufferFlags](kcmblockbufferalwayscopydataflag.md)
  Used with [`CMBlockBuffer`](cmblockbuffer.md) to cause it to always produce an allocated copy of the desired data.
- [var kCMBlockBufferDontOptimizeDepthFlag: CMBlockBufferFlags](kcmblockbufferdontoptimizedepthflag.md)
  Passed to block buffers to suppress reference depth optimization.
- [var kCMBlockBufferPermitEmptyReferenceFlag: CMBlockBufferFlags](kcmblockbufferpermitemptyreferenceflag.md)
  Passed to [`CMBlockBuffer`](cmblockbuffer.md) and [`CMBlockBuffer`](cmblockbuffer.md) to allow references into a `CMBlockBuffer` that may not yet be populated.

## See Also

- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreateempty(allocator:capacity:flags:blockbufferout:).md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithMemoryBlock(allocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that’s backed by a memory block.
- [func CMBlockBufferCreateWithBufferReference(allocator: CFAllocator?, referenceBuffer: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithbufferreference(allocator:referencebuffer:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that refers to another block buffer object.
- [func CMBlockBufferCreateContiguous(allocator: CFAllocator?, sourceBuffer: CMBlockBuffer, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatecontiguous(allocator:sourcebuffer:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that contains a contiguous copy of, or reference to, the data specified by the parameters.
- [Block Buffer Flags](block-buffer-flags.md)
  An enumeration of flags that control behaviors and features of block buffer APIs.
- [struct CMBlockBufferCustomBlockSource](cmblockbuffercustomblocksource.md)
  A structure to support custom memory allocation and deallocation for a block used in a block buffer.
- [Custom Block Source Version](custom-block-source-version.md)
  A custom block source version identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferflags)*