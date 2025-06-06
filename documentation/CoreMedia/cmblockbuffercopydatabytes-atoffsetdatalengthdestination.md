# CMBlockBufferCopyDataBytes(_:atOffset:dataLength:destination:)

**Framework**: Core Media  
**Kind**: func

Copies bytes from a block buffer into a provided memory area.

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
func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer, atOffset offsetToData: Int, dataLength: Int, destination: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if the copy succeeded, returns an error otherwise.

#### Discussion

This function is used to copy bytes out of a `CMBlockBuffer` into a provided piece of memory. It deals with the possibility of the desired range of data being noncontiguous. The function assumes that the memory at the destination is sufficient to hold the data. If `dataLength` bytes of data are not available in the `CMBlockBuffer`, an error is returned and the contents of the destination are undefined.

## Parameters

- `theSourceBuffer`: The buffer from which data will be copied into the destination.
- `offsetToData`: Offset within the source   at which the copy should begin.
- `dataLength`: Number of bytes to copy, starting at  , within the source  . Must not be zero.
- `destination`: Memory into which the data should be copied.

## See Also

- [func CMBlockBufferAppendMemoryBlock(CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendmemoryblock(_:memoryblock:length:blockallocator:customblocksource:offsettodata:datalength:flags:).md)
  Adds a memory block to an existing block buffer.
- [func CMBlockBufferAppendBufferReference(CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendbufferreference(_:targetbbuf:offsettodata:datalength:flags:).md)
  Adds a reference to an existing block buffer.
- [func CMBlockBufferAssureBlockMemory(CMBlockBuffer) -> OSStatus](cmblockbufferassureblockmemory(_:).md)
  Assures that the system allocates memory for all memory blocks in a block buffer.
- [func CMBlockBufferAccessDataBytes(CMBlockBuffer, atOffset: Int, length: Int, temporaryBlock: UnsafeMutableRawPointer, returnedPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](cmblockbufferaccessdatabytes(_:atoffset:length:temporaryblock:returnedpointerout:).md)
  Accesses potentially noncontiguous data in a block buffer.
- [func CMBlockBufferReplaceDataBytes(with: UnsafeRawPointer, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferreplacedatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Copies bytes from a given memory block into a block buffer replacing bytes in the underlying data blocks.
- [func CMBlockBufferFillDataBytes(with: CChar, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferfilldatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Fills the destination buffer with the specified data byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffercopydatabytes(_:atoffset:datalength:destination:))*