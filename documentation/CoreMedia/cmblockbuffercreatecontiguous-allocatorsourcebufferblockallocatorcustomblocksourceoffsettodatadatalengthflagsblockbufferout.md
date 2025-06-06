# CMBlockBufferCreateContiguous(allocator:sourceBuffer:blockAllocator:customBlockSource:offsetToData:dataLength:flags:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a block buffer that contains a contiguous copy of, or reference to, the data specified by the parameters.

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
func CMBlockBufferCreateContiguous(allocator structureAllocator: CFAllocator?, sourceBuffer: CMBlockBuffer, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Produces a `CMBlockBuffer` containing a contiguous copy of or reference to the data specified by the parameters. The resulting new `CMBlockBuffer` may contain an allocated copy of the data, or may contain a contiguous `CMBlockBuffer` reference. If the `kCMBlockBufferAlwaysCopyDataFlag` is set in the flags parameter, the resulting `CMBlockBuffer` will contain an allocated copy of the data rather than a reference to the `SourceBuffer`.

## Parameters

- `structureAllocator`: Allocator to use for allocating the   object.   will cause the default allocator to be used.
- `sourceBuffer`:   from which data will be copied or referenced. Must not be   or empty.
- `blockAllocator`: Allocator to be used for allocating the memory block if a contiguous copy of the data is to be made. Passing   will cause the default allocator (as set at the time of the call) to be used.
- `customBlockSource`: If non- , it will be used for the allocation and freeing of the memory block (the   parameter is ignored). If provided, and the parameter   is set,      routine must be non- . Allocate will be called once, if successful, when the memory block is allocated.   will be called once when the   is disposed.
- `offsetToData`: Offset within the source   at which the new   should obtain data.
- `dataLength`: Number of relevant data bytes, starting at  , within the source  . If zero, the target buffer’s total available   (starting at offsetToData) will be referenced.
- `flags`: Feature and control flags.
- `blockBufferOut`: Receives newly-created   object with a retain count of 1. Must not be   .

## See Also

- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreateempty(allocator:capacity:flags:blockbufferout:).md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithMemoryBlock(allocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that’s backed by a memory block.
- [func CMBlockBufferCreateWithBufferReference(allocator: CFAllocator?, referenceBuffer: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](cmblockbuffercreatewithbufferreference(allocator:referencebuffer:offsettodata:datalength:flags:blockbufferout:).md)
  Creates a block buffer that refers to another block buffer object.
- [typealias CMBlockBufferFlags](cmblockbufferflags.md)
  A type for flags that control behaviors and features of block buffer APIs.
- [Block Buffer Flags](block-buffer-flags.md)
  An enumeration of flags that control behaviors and features of block buffer APIs.
- [struct CMBlockBufferCustomBlockSource](cmblockbuffercustomblocksource.md)
  A structure to support custom memory allocation and deallocation for a block used in a block buffer.
- [Custom Block Source Version](custom-block-source-version.md)
  A custom block source version identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercreatecontiguous(allocator:sourcebuffer:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:))*