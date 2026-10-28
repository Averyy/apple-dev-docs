# CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_:packetDescriptionsPointerOut:sizeOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a pointer to a constant array of audio stream packet descriptions.

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
func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut packetDescriptionsSizeOut: UnsafeMutablePointer<Int>?) -> OSStatus
```

```c
extern OSStatus CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBufferRef sbuf, const AudioStreamPacketDescription **packetDescriptionsPointerOut, size_t *packetDescriptionsSizeOut);
```

## Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

## Discussion

Returns a pointer to (and size of) a constant array of `AudioStreamPacketDescriptions` for the variable bytes per packet or variable frames per packet audio data in the provided `CMSampleBuffer`. The pointer will remain valid as long as the buffer continues to be retained.

Constant bit rate, constant frames-per-packet audio yields a return value of `noErr` and no packet descriptions.

This API is specific to audio format sample buffers, and will return `kCMSampleBufferError_InvalidMediaTypeForOperation` if called with a non-audio sample buffer.

## Parameters

- `sbuf`: The `CMSampleBuffer` being modified.
- `packetDescriptionsPointerOut`: On output, contains pointer to a constant array of `AudioStreamPacketDescriptions`. May be `NULL`.
- `packetDescriptionsSizeOut`: Size in bytes of constant array of `AudioStreamPacketDescriptions`. May be `NULL`.

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
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](./cmsamplebuffersetdatabufferfromaudiobufferlist%28_,blockbufferallocator,blockbuffermemoryallocator,flags,bufferlist%29.md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./cmsamplebuffercopypcmdataintoaudiobufferlist%28_,at,framecount,into%29.md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptions%28_,allocatedsize,packetdescriptionsout,packetdescriptionssizeneededout%29.md)
  Creates an array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:))*