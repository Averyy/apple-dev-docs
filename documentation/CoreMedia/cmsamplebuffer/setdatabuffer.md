# setDataBuffer(_:)

**Framework**: Core Media  
**Kind**: method

Associates a block buffer of media data with a sample buffer.

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
func setDataBuffer(_ dataBuffer: CMBlockBuffer) throws
```

#### Discussion

Calling this method is a write-once operation; it fails if the sample buffer already has a data buffer.

The purpose of this API is to allow you to create a sample buffer with timing and format information, before associating it with media data. For example, some media services may have access to sample size, timing, and format information, but only load the media data when accessed. Such services may create sample buffers with that information and insert them into queues early, and use this API to attach the media data when it’s ready.

## Parameters

- `dataBuffer`: A buffer that contains the media data.

## See Also

- [var dataBuffer: CMBlockBuffer?](cmsamplebuffer/databuffer.md)
  A block buffer that contains the media data.
- [var imageBuffer: CVImageBuffer?](cmsamplebuffer/imagebuffer.md)
  An image buffer that contains the media data.
- [func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags, body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R](cmsamplebuffer/withaudiobufferlist(blockbuffermemoryallocator:flags:body:).md)
  Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/setdatabuffer(_:))*