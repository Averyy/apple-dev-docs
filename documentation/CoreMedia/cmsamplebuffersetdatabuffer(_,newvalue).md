# CMSampleBufferSetDataBuffer(_:newValue:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Sets a block buffer of media data on a sample buffer.

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
func CMSampleBufferSetDataBuffer(_ sbuf: CMSampleBuffer, newValue dataBuffer: CMBlockBuffer) -> OSStatus
```

```c
extern OSStatus CMSampleBufferSetDataBuffer(CMSampleBufferRef sbuf, CMBlockBufferRef dataBuffer);
```

## Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

## Discussion

If successful, this operation retains the `dataBuffer`. This allows the caller to release the `dataBuffer` after calling this API, if it has no further need to reference it. This is a write-once operation; it fails if the `CMSampleBuffer` already has a `dataBuffer`. This API allows a `CMSampleBuffer` to exist, with timing and format information, before the associated data shows up.Example of usage: Some media services may have access to sample size, timing, and format information before the data is read. Such services may create `CMSampleBuffers` with that information and insert them into queues early, and use this API to attach the `CMBlockBuffers` later, when the data becomes ready.

## Parameters

- `sbuf`: The sample buffer being modified.
- `dataBuffer`: `CMBlockBuffer` of data being associated with.

## See Also

### Modifying Sample Buffers
- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](./cmsamplebuffergetdatabuffer%28_%29.md)
  Returns a block buffer that contains the media data.
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
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptionsptr%28_,packetdescriptionspointerout,sizeout%29.md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetdatabuffer(_:newvalue:))*