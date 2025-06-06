# audioStreamPacketDescriptions()

**Framework**: Core Media  
**Kind**: method

Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.

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
func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]
```

#### Return Value

An array of audio stream packet descriptions.

#### Discussion

Constant bit rate, constant frames-per-packet audio yields an empty array.

This API is specific to audio format sample buffers, and throws an [`invalidMediaTypeForOperation`](cmsamplebuffer/error/invalidmediatypeforoperation.md) error if called on a nonaudio sample buffer.

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
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](cmsamplebuffer/copypcmdata(fromrange:into:).md)
  Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](cmsamplebuffer/withunsafeaudiostreampacketdescriptions(_:).md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  A structure that holds all samples in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/audiostreampacketdescriptions())*