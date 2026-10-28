# CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_:bufferListSizeNeededOut:bufferListOut:bufferListSize:blockBufferAllocator:blockBufferMemoryAllocator:flags:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns an audio buffer list that contains the media data.

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
func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator blockBufferStructureAllocator: CFAllocator?, blockBufferMemoryAllocator blockBufferBlockAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus
```

```c
extern OSStatus CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBufferRef sbuf, size_t *bufferListSizeNeededOut, AudioBufferList *bufferListOut, size_t bufferListSize, CFAllocatorRef blockBufferStructureAllocator, CFAllocatorRef blockBufferBlockAllocator, uint32_t flags, CMBlockBufferRef*blockBufferOut);
```

## Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

## Discussion

Creates an `AudioBufferList` containing the data from the `CMSampleBuffer`, and a `CMBlockBuffer` which references (and manages the lifetime of) the data in that `AudioBufferList`. The data may or may not be copied, depending on the contiguity and 16-byte alignment of the sample buffer’s data.

The buffers placed in the `AudioBufferList` are guaranteed to be contiguous.

The buffers in the `AudioBufferList` will be 16-byte-aligned if `kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment` is passed in.

## Parameters

- `sbuf`: `CMSampleBuffer` being accessed.
- `bufferListSizeNeededOut`: Receives the size of the AudioBufferList required to accommodate the data. May be `NULL`.
- `bufferListOut`: Allocated by the caller, sized as specified by `bufferListSizeNeededOut`. It’s filled in with pointers into the retained `blockBufferOut`. May be `NULL`.
- `bufferListSize`: Size of the `bufferListOut` allocated by the client. If `bufferListOut` isn’t `NULL` and `bufferListSize` is insufficient, `kFigSampleBufferError_ArrayTooSmall` is returned.
- `blockBufferStructureAllocator`: Allocator to use when creating the `CMBlockBuffer` structure.
- `blockBufferBlockAllocator`: Allocator to use for memory block held by the `CMBlockBuffer`.
- `flags`: Flags controlling operation.
- `blockBufferOut`: The retained `CMBlockBuffer`.

## See Also

### Modifying Sample Buffers
- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](./cmsamplebuffergetdatabuffer%28_%29.md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](./cmsamplebuffersetdatabuffer%28_,newvalue%29.md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](./cmsamplebuffergetimagebuffer%28_%29.md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](./cmsamplebuffersetdatabufferfromaudiobufferlist%28_,blockbufferallocator,blockbuffermemoryallocator,flags,bufferlist%29.md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./cmsamplebuffercopypcmdataintoaudiobufferlist%28_,at,framecount,into%29.md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptions%28_,allocatedsize,packetdescriptionsout,packetdescriptionssizeneededout%29.md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptionsptr%28_,packetdescriptionspointerout,sizeout%29.md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:))*