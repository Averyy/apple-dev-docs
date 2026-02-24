# CMBlockBufferAppendBufferReference(_:targetBBuf:offsetToData:dataLength:flags:)

**Framework**: Core Media  
**Kind**: func

Adds a reference to an existing block buffer.

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
func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Adds a buffer reference of (a possibly subset portion of) another `CMBlockBuffer`, the target `CMBlockBuffer`, to an existing `CMBlockBuffer`. The existing `CMBlockBuffer's` total data length will be increased by the specified `dataLength`. Note that append operations are not thread safe, so care must be taken when appending to block buffers that are used by multiple threads.

## Parameters

- `theBuffer`: The existing `CMBlockBuffer`.  The target `CMBlockBuffer` will be added to the memory being managed by `theBuffer` (the existing `CMBlockBuffer`). Must not be `NULL`.
- `targetBBuf`: The target `CMBlockBuffer`. The target `CMBlockBuffer` will be added to the memory managed by the `theBuffer` (the existing`CMBlockBuffer`).This parameter must not be `NULL`. Unless the `kCMBlockBufferPermitEmptyReferenceFlag` is passed, the target `CMBlockBuffer` must not be empty and it must have a data length at least large enough to supply the data subset specified (i.e. `offsetToData` + `dataLength` bytes).
- `offsetToData`: The reference maintained by the existing `CMBlockBuffer` will begin after this offset within the target `CMBlockBuffer`.
- `dataLength`: Number of relevant data bytes, starting at `offsetToData`, within the target `CMBlockBuffer`. If zero, the target buffer’s total available `dataLength` (starting at offsetToData) will be referenced.
- `flags`: Feature and control flags.

## See Also

- [func CMBlockBufferAppendMemoryBlock(CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendmemoryblock(_:memoryblock:length:blockallocator:customblocksource:offsettodata:datalength:flags:).md)
  Adds a memory block to an existing block buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferappendbufferreference(_:targetbbuf:offsettodata:datalength:flags:))*