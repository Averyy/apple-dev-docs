# CMBlockBufferFillDataBytes(with:blockBuffer:offsetIntoDestination:dataLength:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Fills the destination buffer with the specified data byte.

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
func CMBlockBufferFillDataBytes(with fillByte: CChar, blockBuffer destinationBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus
```

```c
extern OSStatus CMBlockBufferFillDataBytes(char fillByte, CMBlockBufferRef destinationBuffer, size_t offsetIntoDestination, size_t dataLength);
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

## Parameters

- `fillByte`: The data byte with which to fill the destination buffer.
- `destinationBuffer`: `CMBlockBuffer` into which the data bytes are filled.
- `offsetIntoDestination`: Start of data area for the buffer.
- `dataLength`: Length of the valid data area for the buffer.

## See Also

### Modifying a Block Buffer
- [func CMBlockBufferAppendMemoryBlock(CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](./cmblockbufferappendmemoryblock%28_,memoryblock,length,blockallocator,customblocksource,offsettodata,datalength,flags%29.md)
  Adds a memory block to an existing block buffer.
- [func CMBlockBufferAppendBufferReference(CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](./cmblockbufferappendbufferreference%28_,targetbbuf,offsettodata,datalength,flags%29.md)
  Adds a reference to an existing block buffer.
- [func CMBlockBufferAssureBlockMemory(CMBlockBuffer) -> OSStatus](./cmblockbufferassureblockmemory%28_%29.md)
  Assures that the system allocates memory for all memory blocks in a block buffer.
- [func CMBlockBufferAccessDataBytes(CMBlockBuffer, atOffset: Int, length: Int, temporaryBlock: UnsafeMutableRawPointer, returnedPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./cmblockbufferaccessdatabytes%28_,atoffset,length,temporaryblock,returnedpointerout%29.md)
  Accesses potentially noncontiguous data in a block buffer.
- [func CMBlockBufferCopyDataBytes(CMBlockBuffer, atOffset: Int, dataLength: Int, destination: UnsafeMutableRawPointer) -> OSStatus](./cmblockbuffercopydatabytes%28_,atoffset,datalength,destination%29.md)
  Copies bytes from a block buffer into a provided memory area.
- [func CMBlockBufferReplaceDataBytes(with: UnsafeRawPointer, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](./cmblockbufferreplacedatabytes%28with,blockbuffer,offsetintodestination,datalength%29.md)
  Copies bytes from a given memory block into a block buffer replacing bytes in the underlying data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferfilldatabytes(with:blockbuffer:offsetintodestination:datalength:))*