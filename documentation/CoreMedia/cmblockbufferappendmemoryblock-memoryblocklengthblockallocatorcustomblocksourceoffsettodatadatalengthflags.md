# CMBlockBufferAppendMemoryBlock(_:memoryBlock:length:blockAllocator:customBlockSource:offsetToData:dataLength:flags:)

**Framework**: Core Media  
**Kind**: func

Adds a memory block to an existing block buffer.

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
func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length blockLength: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Adds a `memoryBlock` to an existing `CMBlockBuffer`. The memory block may be statically allocated, dynamically allocated using the given allocator or not yet allocated. The `CMBlockBuffer's` total data length will be increased by the specified `dataLength`. If the `kCMBlockBufferAssureMemoryNowFlag` is set in the flags parameter, the memory block is allocated immediately using the `blockAllocator` or `customBlockSource`. Note that append operations are not thread safe, so care must be taken when appending to block buffers that are used by multiple threads.

## Parameters

- `theBuffer`: The existing   to which the new   will be added. Must not be 
- `memoryBlock`: Block of memory to hold buffered data. If  , a memory block will be allocated when needed (via a call to  ) using the provided   or  . If non- , the block will be used and will be deallocated when the   is finalized (i.e. released for the last time).
- `blockLength`: Overall length of the memory block in bytes. Must not be zero. This is the size of the supplied   or the size to allocate if   is  .
- `blockAllocator`: Allocator to be used for allocating the  , if   is  . If   is non- , this allocator will be used to deallocate it, if provided. Passing   will cause the default allocator (as set at the time of the call) to be used. Pass   if no deallocation is desired.
- `customBlockSource`: If non-NULL, it will be used for the allocation and freeing of the memory block (the   parameter is ignored). If provided, and the   parameter is  , its   routine must be non- . Allocate will be called once, if successful, when the   is allocated.   will be called once when the   is disposed.
- `offsetToData`: The reference maintained by the existing   will begin after this offset within the   .
- `dataLength`: Number of relevant data bytes, starting at  , within the memory block.
- `flags`: Feature and control flags

## See Also

- [func CMBlockBufferAppendBufferReference(CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendbufferreference(_:targetbbuf:offsettodata:datalength:flags:).md)
  Adds a reference to an existing block buffer.
- [func CMBlockBufferAssureBlockMemory(CMBlockBuffer) -> OSStatus](cmblockbufferassureblockmemory(_:).md)
  Assures that the system allocates memory for all memory blocks in a block buffer.
- [func CMBlockBufferAccessDataBytes(CMBlockBuffer, atOffset: Int, length: Int, temporaryBlock: UnsafeMutableRawPointer, returnedPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](cmblockbufferaccessdatabytes(_:atoffset:length:temporaryblock:returnedpointerout:).md)
  Accesses potentially noncontiguous data in a block buffer.
- [func CMBlockBufferCopyDataBytes(CMBlockBuffer, atOffset: Int, dataLength: Int, destination: UnsafeMutableRawPointer) -> OSStatus](cmblockbuffercopydatabytes(_:atoffset:datalength:destination:).md)
  Copies bytes from a block buffer into a provided memory area.
- [func CMBlockBufferReplaceDataBytes(with: UnsafeRawPointer, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferreplacedatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Copies bytes from a given memory block into a block buffer replacing bytes in the underlying data blocks.
- [func CMBlockBufferFillDataBytes(with: CChar, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferfilldatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Fills the destination buffer with the specified data byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferappendmemoryblock(_:memoryblock:length:blockallocator:customblocksource:offsettodata:datalength:flags:))*