# audioStreamPacketDescriptions()

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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

This API is specific to audio format sample buffers, and throws an [`invalidMediaTypeForOperation`](./error/invalidmediatypeforoperation.md) error if called on a nonaudio sample buffer.

## See Also

### Modifying Sample Buffers
- [var dataBuffer: CMBlockBuffer?](./databuffer.md)
  A block buffer that contains the media data.
- [func setDataBuffer(CMBlockBuffer) throws](./setdatabuffer%28_%29.md)
  Associates a block buffer of media data with a sample buffer.
- [var imageBuffer: CVImageBuffer?](./imagebuffer.md)
  An image buffer that contains the media data.
- [func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags, body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R](./withaudiobufferlist%28blockbuffermemoryallocator,flags,body%29.md)
  Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.
- [func setDataBuffer(fromAudioBufferList: UnsafePointer<AudioBufferList>, blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags) throws](./setdatabuffer%28fromaudiobufferlist,blockbuffermemoryallocator,flags%29.md)
  Creates a block buffer that contains a copy of the data from an audio buffer list, and sets it as the sample buffer’s data.
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](./copypcmdata%28fromrange,into%29.md)
  Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](./withunsafeaudiostreampacketdescriptions%28_%29.md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](./singlesamplebuffers%28%29.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](./singlesamplebuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/audiostreampacketdescriptions())*