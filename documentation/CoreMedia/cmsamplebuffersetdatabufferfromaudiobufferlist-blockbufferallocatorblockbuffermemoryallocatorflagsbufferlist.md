# CMSampleBufferSetDataBufferFromAudioBufferList(_:blockBufferAllocator:blockBufferMemoryAllocator:flags:bufferList:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

Creates a `CMBlockBuffer` containing a copy of the data from the `AudioBufferList`, and sets that as the sample buffer’s data buffer. The resulting buffer(s) in the sample buffer will be 16-byte-aligned if `kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment` is passed in.

## Parameters

- `sbuf`: The   being modified.
- `blockBufferStructureAllocator`: Allocator to use when creating the   structure.
- `blockBufferBlockAllocator`: Allocator to use for memory block held by the  .
- `flags`: Flags controlling operation.
- `bufferList`: Buffer list whose data will be copied into the new  .

## See Also

- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](cmsamplebuffergetdatabuffer(_:).md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](cmsamplebuffersetdatabuffer(_:newvalue:).md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](cmsamplebuffergetimagebuffer(_:).md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:).md)
  Returns an audio buffer list that contains the media data.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](cmsamplebuffercopypcmdataintoaudiobufferlist(_:at:framecount:into:).md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptions(_:allocatedsize:packetdescriptionsout:packetdescriptionssizeneededout:).md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:).md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:))*