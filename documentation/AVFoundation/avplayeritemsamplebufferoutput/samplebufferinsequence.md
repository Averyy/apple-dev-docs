# AVPlayerItemSampleBufferOutput.SampleBufferInSequence

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Holds the information necessary for processing generated sample buffers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct SampleBufferInSequence
```

## Topics

### Initializers
- [init(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>, sequenceWasRestarted: Bool)](./samplebufferinsequence/init%28samplebuffer,sequencewasrestarted%29.md)
### Instance Properties
- [var sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>](./samplebufferinsequence/samplebuffer.md)
  Sample buffer containing media data.
- [var sequenceWasRestarted: Bool](./samplebufferinsequence/sequencewasrestarted.md)
  Indicates the very first buffer in a new sequence produced by this output. Seeking or changing playback direction will start a new sequence of buffers. If you have any sample buffers queued from the previous sequence, these should be discarded.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving sample buffers
- [func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](./nextavailablesamplebuffer%28%29.md)
  Returns the next sample buffer if it is already available.
- [func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](./nextsamplebuffer%28%29.md)
  Returns next sample buffer once it becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence)*