# withAudioBufferList(blockBufferMemoryAllocator:flags:body:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.

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
func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator? = kCFAllocatorDefault, flags: CMSampleBuffer.Flags = [], body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R
```

## Discussion

The system may not copy the data, depending on its contiguity and 16-byte alignment. It guarantees the buffers it places in the AudioBufferList are contiguous.

The system returns 16-byte-aligned buffers if you pass the [`audioBufferListAssure16ByteAlignment`](./flags/audiobufferlistassure16bytealignment.md) flag.

## Parameters

- `blockBufferMemoryAllocator`: An allocator to use for the memory block held by a [CMBlockBuffer](../cmblockbuffer-api.md).
- `flags`: Optional flags that control the operation.
- `body`: A closure the system calls that contains a pointer to an [`AudioBufferList`](../../CoreAudioTypes/audiobufferlist.md) and the block buffer that backs its audio buffers.

## See Also

### Modifying Sample Buffers
- [var dataBuffer: CMBlockBuffer?](./databuffer.md)
  A block buffer that contains the media data.
- [func setDataBuffer(CMBlockBuffer) throws](./setdatabuffer%28_%29.md)
  Associates a block buffer of media data with a sample buffer.
- [var imageBuffer: CVImageBuffer?](./imagebuffer.md)
  An image buffer that contains the media data.
- [func setDataBuffer(fromAudioBufferList: UnsafePointer<AudioBufferList>, blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags) throws](./setdatabuffer%28fromaudiobufferlist,blockbuffermemoryallocator,flags%29.md)
  Creates a block buffer that contains a copy of the data from an audio buffer list, and sets it as the sample buffer’s data.
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](./copypcmdata%28fromrange,into%29.md)
  Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.
- [func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]](./audiostreampacketdescriptions%28%29.md)
  Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](./withunsafeaudiostreampacketdescriptions%28_%29.md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](./singlesamplebuffers%28%29.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](./singlesamplebuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/withaudiobufferlist(blockbuffermemoryallocator:flags:body:))*