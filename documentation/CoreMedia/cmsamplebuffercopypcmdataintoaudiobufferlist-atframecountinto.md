# CMSampleBufferCopyPCMDataIntoAudioBufferList(_:at:frameCount:into:)

**Framework**: Core Media  
**Kind**: func

Copies PCM audio data from a sample buffer into an audio buffer list.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferCopyPCMDataIntoAudioBufferList(_ sbuf: CMSampleBuffer, at frameOffset: Int32, frameCount numFrames: Int32, into bufferList: UnsafeMutablePointer<AudioBufferList>) -> OSStatus
```

#### Discussion

The [`AudioBufferList`](https://developer.apple.com/documentation/CoreAudioTypes/AudioBufferList) must contain the same number of channels and its data buffers must be sized to hold the specified number of frames.

This API is specific to audio format sample buffers, and will return `kCMSampleBufferError_InvalidMediaTypeForOperation` if called with a non-audio sample buffer. It will return an error if the sample buffer doesn’t contain PCM audio data or if its data buffer isn’t ready.

## Parameters

- `sbuf`: The sample buffer containing the PCM audio data to be copied.
- `frameOffset`: The frame offset number from which to begin the copy.
- `numFrames`: The total number of frames to copy.
- `bufferList`: The audio buffer list to populate.

## See Also

- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](cmsamplebuffergetdatabuffer(_:).md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](cmsamplebuffersetdatabuffer(_:newvalue:).md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](cmsamplebuffergetimagebuffer(_:).md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:).md)
  Returns an audio buffer list that contains the media data.
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptions(_:allocatedsize:packetdescriptionsout:packetdescriptionssizeneededout:).md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:).md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercopypcmdataintoaudiobufferlist(_:at:framecount:into:))*