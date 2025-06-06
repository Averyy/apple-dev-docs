# CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_:bufferListSizeNeededOut:bufferListOut:bufferListSize:blockBufferAllocator:blockBufferMemoryAllocator:flags:blockBufferOut:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

Creates an `AudioBufferList` containing the data from the `CMSampleBuffer`, and a `CMBlockBuffer` which references (and manages the lifetime of) the data in that `AudioBufferList`. The data may or may not be copied, depending on the contiguity and 16-byte alignment of the sample buffer’s data.

The buffers placed in the `AudioBufferList` are guaranteed to be contiguous.

The buffers in the `AudioBufferList` will be 16-byte-aligned if `kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment` is passed in.

## Parameters

- `sbuf`:   being accessed.
- `bufferListSizeNeededOut`: Receives the size of the AudioBufferList required to accommodate the data. May be  .
- `bufferListOut`: Allocated by the caller, sized as specified by  . It’s filled in with pointers into the retained  . May be  .
- `bufferListSize`: Size of the   allocated by the client. If   isn’t   and   is insufficient,   is returned.
- `blockBufferStructureAllocator`: Allocator to use when creating the   structure.
- `blockBufferBlockAllocator`: Allocator to use for memory block held by the  .
- `flags`: Flags controlling operation.
- `blockBufferOut`: The retained  .

## See Also

- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](cmsamplebuffergetdatabuffer(_:).md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](cmsamplebuffersetdatabuffer(_:newvalue:).md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](cmsamplebuffergetimagebuffer(_:).md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](cmsamplebuffercopypcmdataintoaudiobufferlist(_:at:framecount:into:).md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptions(_:allocatedsize:packetdescriptionsout:packetdescriptionssizeneededout:).md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:).md)
  Returns a pointer to a constant array of audio stream packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:))*