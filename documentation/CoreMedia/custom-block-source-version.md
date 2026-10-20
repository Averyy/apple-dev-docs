# Custom Block Source Version

**Framework**: Core Media  
**Role**: API Collection

A custom block source version identifier.

## Topics

### Constants
- [var kCMBlockBufferCustomBlockSourceVersion: UInt32](./kcmblockbuffercustomblocksourceversion.md)
  The value is the block source version.

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
- [Block Buffer Flags](./block-buffer-flags.md)
  An enumeration of flags that control behaviors and features of block buffer APIs.
- [struct CMBlockBufferCustomBlockSource](./cmblockbuffercustomblocksource.md)
  A structure to support custom memory allocation and deallocation for a block used in a block buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/custom-block-source-version)*