# CMBlockBufferCreateWithBufferReference(allocator:referenceBuffer:offsetToData:dataLength:flags:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a block buffer that refers to another block buffer object.

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
func CMBlockBufferCreateWithBufferReference(allocator structureAllocator: CFAllocator?, referenceBuffer bufferReference: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Creates a new `CMBlockBuffer` that refers to (a possibly subset portion of) another `CMBlockBuffer`. The returned `CMBlockBuffer` may be further expanded using [`CMBlockBufferAppendMemoryBlock(_:memoryBlock:length:blockAllocator:customBlockSource:offsetToData:dataLength:flags:)`](cmblockbufferappendmemoryblock(_:memoryblock:length:blockallocator:customblocksource:offsettodata:datalength:flags:).md) and/or [`CMBlockBufferAppendBufferReference(_:targetBBuf:offsetToData:dataLength:flags:)`](cmblockbufferappendbufferreference(_:targetbbuf:offsettodata:datalength:flags:).md).

## Parameters

- `structureAllocator`: Allocator to use for allocating the   object.   will cause the default allocator to be used.
- `bufferReference`: The target  . This parameter must not be  . Unless the   is passed, it must not be empty and it must have a data length at least large enough to supply the data subset specified (i.e. offsetToData+dataLength bytes).
- `offsetToData`: Offset within the target   at which the new   should refer to data.
- `dataLength`: Number of relevant data bytes, starting at  , within the target  .
- `flags`: Feature and control flags.
- `blockBufferOut`: Receives newly-created   object with a retain count of 1. Must not be   .

## See Also

- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreateempty(allocator:capacity:flags:blockbufferout:).md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithMemoryBlock(allocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that’s backed by a memory block.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercreatewithbufferreference(allocator:referencebuffer:offsettodata:datalength:flags:blockbufferout:))*