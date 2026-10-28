# singleSampleBuffers()

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns all samples in a sample buffer.

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
func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers
```

## Return Value

All samples from the buffer.

## Discussion

The system creates temporary sample buffers for individual samples that refer to the sample data and containing its timing, size, and attachments.

If there are no sample sizes in the provided sample buffer, the system throws a [`kCMSampleBufferError_CannotSubdivide`](../kcmsamplebuffererror_cannotsubdivide.md) error. This happens, for example, if the samples in the buffer are noncontiguous, such as noninterleaved audio.

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
- [func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]](./audiostreampacketdescriptions%28%29.md)
  Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](./withunsafeaudiostreampacketdescriptions%28_%29.md)
  Calls a closure with an audio stream packet description.
- [CMSampleBuffer.SingleSampleBuffers](./singlesamplebuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/singlesamplebuffers())*