# CMSampleBufferGetImageBuffer(_:)

**Framework**: Core Media  
**Kind**: func

Returns an image buffer that contains the media data.

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
func CMSampleBufferGetImageBuffer(_ sbuf: CMSampleBuffer) -> CVImageBuffer?
```

#### Return Value

`CVImageBuffer` of media data. The result will be `NULL` if the `CMSampleBuffer` does not contain a `CVImageBuffer`, if the `CMSampleBuffer` contains a `CMBlockBuffer`, or if there is some other error.

#### Discussion

The caller doesn’t own the returned buffer, and must retain it explicitly if the caller needs to maintain a reference to it.

## Parameters

- `sbuf`: The   being interrogated.

## See Also

- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](cmsamplebuffergetdatabuffer(_:).md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](cmsamplebuffersetdatabuffer(_:newvalue:).md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:).md)
  Returns an audio buffer list that contains the media data.
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](cmsamplebuffercopypcmdataintoaudiobufferlist(_:at:framecount:into:).md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptions(_:allocatedsize:packetdescriptionsout:packetdescriptionssizeneededout:).md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:).md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetimagebuffer(_:))*