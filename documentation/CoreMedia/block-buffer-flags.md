# Block Buffer Flags

**Framework**: Core Media  
**Role**: API Collection

An enumeration of flags that control behaviors and features of block buffer APIs.

## Topics

### Constants
- [var kCMBlockBufferAssureMemoryNowFlag: CMBlockBufferFlags](./kcmblockbufferassurememorynowflag.md)
  When passed to routines that accept block allocators, causes the memory block to be allocated immediately.
- [var kCMBlockBufferAlwaysCopyDataFlag: CMBlockBufferFlags](./kcmblockbufferalwayscopydataflag.md)
  Used with [`CMBlockBuffer`](./cmblockbuffer.md) to cause it to always produce an allocated copy of the desired data.
- [var kCMBlockBufferDontOptimizeDepthFlag: CMBlockBufferFlags](./kcmblockbufferdontoptimizedepthflag.md)
  Passed to block buffers to suppress reference depth optimization.
- [var kCMBlockBufferPermitEmptyReferenceFlag: CMBlockBufferFlags](./kcmblockbufferpermitemptyreferenceflag.md)
  Passed to [`CMBlockBuffer`](./cmblockbuffer.md) and [`CMBlockBuffer`](./cmblockbuffer.md) to allow references into a `CMBlockBuffer` that may not yet be populated.

## See Also

### Creating a Block Buffer
- [func CMBlockBufferCreateEmpty(allocator: CFAllocator?, capacity: UInt32, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmblockbuffercreateempty%28allocator,capacity,flags,blockbufferout%29.md)
  Creates an empty block buffer.
- [func CMBlockBufferCreateWithMemoryBlock(allocator: CFAllocator?, memoryBlock: UnsafeMutableRawPointer?, blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmblockbuffercreatewithmemoryblock%28allocator,memoryblock,blocklength,blockallocator,customblocksource,offsettodata,datalength,flags,blockbufferout%29.md)
  Creates a block buffer that’s backed by a memory block.
- [func CMBlockBufferCreateWithBufferReference(allocator: CFAllocator?, referenceBuffer: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmblockbuffercreatewithbufferreference%28allocator,referencebuffer,offsettodata,datalength,flags,blockbufferout%29.md)
  Creates a block buffer that refers to another block buffer object.
- [func CMBlockBufferCreateContiguous(allocator: CFAllocator?, sourceBuffer: CMBlockBuffer, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](./cmblockbuffercreatecontiguous%28allocator,sourcebuffer,blockallocator,customblocksource,offsettodata,datalength,flags,blockbufferout%29.md)
  Creates a block buffer that contains a contiguous copy of, or reference to, the data specified by the parameters.
- [typealias CMBlockBufferFlags](./cmblockbufferflags.md)
  A type for flags that control behaviors and features of block buffer APIs.
- [struct CMBlockBufferCustomBlockSource](./cmblockbuffercustomblocksource.md)
  A structure to support custom memory allocation and deallocation for a block used in a block buffer.
- [Custom Block Source Version](./custom-block-source-version.md)
  A custom block source version identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/block-buffer-flags)*