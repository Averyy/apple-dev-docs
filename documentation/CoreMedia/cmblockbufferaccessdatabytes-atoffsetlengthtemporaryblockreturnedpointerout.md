# CMBlockBufferAccessDataBytes(_:atOffset:length:temporaryBlock:returnedPointerOut:)

**Framework**: Core Media  
**Kind**: func

Accesses potentially noncontiguous data in a block buffer.

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
func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer, atOffset offset: Int, length: Int, temporaryBlock: UnsafeMutableRawPointer, returnedPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if the desired amount of data could be accessed at the given offset.

#### Discussion

This routine is use for accessing contiguous and noncontiguous data. If the data is contiguous, the routine will return a pointer to the given `CMBlockBuffer`.  If the data is not contiguous, the routine will copy the data into a temporary block and a pointer to this block will be returned.

## Parameters

- `theBuffer`:   to operate on. Must not be  .
- `offset`: Offset within the   offset range.
- `length`: Desired number of bytes to access at offset.
- `temporaryBlock`: A piece of memory, assumed to be at least   bytes in size. Must not be 
- `returnedPointerOut`: Receives   if the desired amount of data could not be accessed at the given offset. Receives non-  if it could. The value returned is either a direct pointer into the   or to the  . Must not be  .

## See Also

- [func CMBlockBufferAppendMemoryBlock(CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendmemoryblock(_:memoryblock:length:blockallocator:customblocksource:offsettodata:datalength:flags:).md)
  Adds a memory block to an existing block buffer.
- [func CMBlockBufferAppendBufferReference(CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](cmblockbufferappendbufferreference(_:targetbbuf:offsettodata:datalength:flags:).md)
  Adds a reference to an existing block buffer.
- [func CMBlockBufferAssureBlockMemory(CMBlockBuffer) -> OSStatus](cmblockbufferassureblockmemory(_:).md)
  Assures that the system allocates memory for all memory blocks in a block buffer.
- [func CMBlockBufferCopyDataBytes(CMBlockBuffer, atOffset: Int, dataLength: Int, destination: UnsafeMutableRawPointer) -> OSStatus](cmblockbuffercopydatabytes(_:atoffset:datalength:destination:).md)
  Copies bytes from a block buffer into a provided memory area.
- [func CMBlockBufferReplaceDataBytes(with: UnsafeRawPointer, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferreplacedatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Copies bytes from a given memory block into a block buffer replacing bytes in the underlying data blocks.
- [func CMBlockBufferFillDataBytes(with: CChar, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](cmblockbufferfilldatabytes(with:blockbuffer:offsetintodestination:datalength:).md)
  Fills the destination buffer with the specified data byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferaccessdatabytes(_:atoffset:length:temporaryblock:returnedpointerout:))*