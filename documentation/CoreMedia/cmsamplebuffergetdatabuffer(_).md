# CMSampleBufferGetDataBuffer(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a block buffer that contains the media data.

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
func CMSampleBufferGetDataBuffer(_ sbuf: CMSampleBuffer) -> CMBlockBuffer?
```

```c
extern CMBlockBufferRefCMSampleBufferGetDataBuffer(CMSampleBufferRef sbuf);
```

## Return Value

`CMBlockBuffer` of media data. The result will be `NULL` if the `CMSampleBuffer` does not contain a `CMBlockBuffer`, if the `CMSampleBuffer` contains a `CVImageBuffer`, or if there is some other error.

## Discussion

The caller doesn’t own the returned `dataBuffer`, and must retain it explicitly if the caller needs to maintain a reference to it.

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.

## See Also

### Modifying Sample Buffers
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
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](./cmsamplebuffergetaudiostreampacketdescriptionsptr%28_,packetdescriptionspointerout,sizeout%29.md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetdatabuffer(_:))*