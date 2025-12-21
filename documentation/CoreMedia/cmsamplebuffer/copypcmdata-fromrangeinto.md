# copyPCMData(fromRange:into:)

**Framework**: Core Media  
**Kind**: method

Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.

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
func copyPCMData(fromRange range: Range<Int>, into bufferList: UnsafeMutablePointer<AudioBufferList>) throws
```

#### Discussion

The audio buffer list must contain the same number of channels, and must be appropriately sized for its data buffers to hold the specified number of frames. This API is specific to audio format sample buffers, and throws an [`invalidMediaTypeForOperation`](cmsamplebuffer/error/invalidmediatypeforoperation.md) if called with a nonaudio sample buffer. Likewise, this method throws an error if the sample buffer doesn’t contain PCM audio data or if its data buffer isn’t ready.

## Parameters

- `range`: The range of the data buffer to copy from.
- `bufferList`: The audio buffer list to populate.

## See Also

- [var dataBuffer: CMBlockBuffer?](cmsamplebuffer/databuffer.md)
  A block buffer that contains the media data.
- [func setDataBuffer(CMBlockBuffer) throws](cmsamplebuffer/setdatabuffer(_:).md)
  Associates a block buffer of media data with a sample buffer.
- [var imageBuffer: CVImageBuffer?](cmsamplebuffer/imagebuffer.md)
  An image buffer that contains the media data.
- [func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags, body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R](cmsamplebuffer/withaudiobufferlist(blockbuffermemoryallocator:flags:body:).md)
  Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.
- [func setDataBuffer(fromAudioBufferList: UnsafePointer<AudioBufferList>, blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags) throws](cmsamplebuffer/setdatabuffer(fromaudiobufferlist:blockbuffermemoryallocator:flags:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list, and sets it as the sample buffer’s data.
- [func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]](cmsamplebuffer/audiostreampacketdescriptions.md)
  Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](cmsamplebuffer/withunsafeaudiostreampacketdescriptions(_:).md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/copypcmdata(fromrange:into:))*