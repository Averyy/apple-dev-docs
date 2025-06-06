# withAudioBufferList(blockBufferMemoryAllocator:flags:body:)

**Framework**: Core Media  
**Kind**: method

Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator? = kCFAllocatorDefault, flags: CMSampleBuffer.Flags = [], body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R
```

#### Discussion

The system may not copy the data, depending on its contiguity and 16-byte alignment. It guarantees the buffers it places in the AudioBufferList are contiguous.

The system returns 16-byte-aligned buffers if you pass the [`audioBufferListAssure16ByteAlignment`](cmsamplebuffer/flags/audiobufferlistassure16bytealignment.md) flag.

## Parameters

- `blockBufferMemoryAllocator`: An allocator to use for the memory block held by a  .
- `flags`: Optional flags that control the operation.
- `body`: A closure the system calls that contains a pointer to an   and the block buffer that backs its audio buffers.

## See Also

- [var dataBuffer: CMBlockBuffer?](cmsamplebuffer/databuffer.md)
  A block buffer that contains the media data.
- [func setDataBuffer(CMBlockBuffer) throws](cmsamplebuffer/setdatabuffer(_:).md)
  Associates a block buffer of media data with a sample buffer.
- [var imageBuffer: CVImageBuffer?](cmsamplebuffer/imagebuffer.md)
  An image buffer that contains the media data.
- [func setDataBuffer(fromAudioBufferList: UnsafePointer<AudioBufferList>, blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags) throws](cmsamplebuffer/setdatabuffer(fromaudiobufferlist:blockbuffermemoryallocator:flags:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list, and sets it as the sample buffer’s data.
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](cmsamplebuffer/copypcmdata(fromrange:into:).md)
  Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.
- [func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]](cmsamplebuffer/audiostreampacketdescriptions.md)
  Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](cmsamplebuffer/withunsafeaudiostreampacketdescriptions(_:).md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  A structure that holds all samples in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/withaudiobufferlist(blockbuffermemoryallocator:flags:body:))*