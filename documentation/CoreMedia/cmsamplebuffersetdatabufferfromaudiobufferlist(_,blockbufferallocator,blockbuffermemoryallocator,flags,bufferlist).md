# CMSampleBufferSetDataBufferFromAudioBufferList(_:blockBufferAllocator:blockBufferMemoryAllocator:flags:bufferList:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a block buffer that contains a copy of the data from an audio buffer list.

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
func CMSampleBufferSetDataBufferFromAudioBufferList(_ sbuf: CMSampleBuffer, blockBufferAllocator blockBufferStructureAllocator: CFAllocator?, blockBufferMemoryAllocator blockBufferBlockAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus
```

```c
extern OSStatus CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBufferRef sbuf, CFAllocatorRef blockBufferStructureAllocator, CFAllocatorRef blockBufferBlockAllocator, uint32_t flags, const AudioBufferList *bufferList);
```

#### Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

#### Discussion

Creates a `CMBlockBuffer` containing a copy of the data from the `AudioBufferList`, and sets that as the sample buffer’s data buffer. The resulting buffer(s) in the sample buffer will be 16-byte-aligned if `kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment` is passed in.

## Parameters

- `sbuf`: The `CMSampleBuffer` being modified.
- `blockBufferStructureAllocator`: Allocator to use when creating the `CMBlockBuffer` structure.
- `blockBufferBlockAllocator`: Allocator to use for memory block held by the `CMBlockBuffer`.
- `flags`: Flags controlling operation.
- `bufferList`: Buffer list whose data will be copied into the new `CMBlockBuffer`.

## See Also

### Modifying Sample Buffers
- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](./cmsamplebuffergetdatabuffer%28_%29.md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](./cmsamplebuffersetdatabuffer%28_,newvalue%29.md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](./cmsamplebuffergetimagebuffer%28_%29.md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](./cmsamplebuffergetaudiobufferlistwithretainedblockbuffer%28_,bufferlistsizeneededout,bufferlistout,bufferlistsize,blockbufferallocator,blockbuffermemoryallocator,flags,blockbufferout%29.md)
  Returns an audio buffer list that contains the media data.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./cmsamplebuffercopypcmdataintoaudiobufferlist%28_,at,framecount,into%29.md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptions%28_,allocatedsize,packetdescriptionsout,packetdescriptionssizeneededout%29.md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptionsptr%28_,packetdescriptionspointerout,sizeout%29.md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:))*