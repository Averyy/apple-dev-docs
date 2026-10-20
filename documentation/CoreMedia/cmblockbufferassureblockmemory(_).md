# CMBlockBufferAssureBlockMemory(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Assures that the system allocates memory for all memory blocks in a block buffer.

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
func CMBlockBufferAssureBlockMemory(_ theBuffer: CMBlockBuffer) -> OSStatus
```

```c
extern OSStatus CMBlockBufferAssureBlockMemory(CMBlockBufferRef theBuffer);
```

#### Return Value

Returns `kCMBlockBufferNoErr` if successful.

#### Discussion

Traverses the possibly complex `CMBlockBuffer`, allocating the memory for any constituent memory blocks that are not yet allocated.

## Parameters

- `theBuffer`: `CMBlockBuffer` to operate on. Must not be `NULL`.

## See Also

### Modifying a Block Buffer
- [func CMBlockBufferAppendMemoryBlock(CMBlockBuffer, memoryBlock: UnsafeMutableRawPointer?, length: Int, blockAllocator: CFAllocator?, customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>?, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](./cmblockbufferappendmemoryblock%28_,memoryblock,length,blockallocator,customblocksource,offsettodata,datalength,flags%29.md)
  Adds a memory block to an existing block buffer.
- [func CMBlockBufferAppendBufferReference(CMBlockBuffer, targetBBuf: CMBlockBuffer, offsetToData: Int, dataLength: Int, flags: CMBlockBufferFlags) -> OSStatus](./cmblockbufferappendbufferreference%28_,targetbbuf,offsettodata,datalength,flags%29.md)
  Adds a reference to an existing block buffer.
- [func CMBlockBufferAccessDataBytes(CMBlockBuffer, atOffset: Int, length: Int, temporaryBlock: UnsafeMutableRawPointer, returnedPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> OSStatus](./cmblockbufferaccessdatabytes%28_,atoffset,length,temporaryblock,returnedpointerout%29.md)
  Accesses potentially noncontiguous data in a block buffer.
- [func CMBlockBufferCopyDataBytes(CMBlockBuffer, atOffset: Int, dataLength: Int, destination: UnsafeMutableRawPointer) -> OSStatus](./cmblockbuffercopydatabytes%28_,atoffset,datalength,destination%29.md)
  Copies bytes from a block buffer into a provided memory area.
- [func CMBlockBufferReplaceDataBytes(with: UnsafeRawPointer, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](./cmblockbufferreplacedatabytes%28with,blockbuffer,offsetintodestination,datalength%29.md)
  Copies bytes from a given memory block into a block buffer replacing bytes in the underlying data blocks.
- [func CMBlockBufferFillDataBytes(with: CChar, blockBuffer: CMBlockBuffer, offsetIntoDestination: Int, dataLength: Int) -> OSStatus](./cmblockbufferfilldatabytes%28with,blockbuffer,offsetintodestination,datalength%29.md)
  Fills the destination buffer with the specified data byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferassureblockmemory(_:))*