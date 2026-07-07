# AVPlayerItemSampleBufferOutput.SampleBufferInSequence

**Framework**: AVFoundation  
**Kind**: struct

Holds the information necessary for processing generated sample buffers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct SampleBufferInSequence
```

## Topics

### Initializers
- [init(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>, sequenceWasRestarted: Bool)](avplayeritemsamplebufferoutput/samplebufferinsequence/init(samplebuffer:sequencewasrestarted:).md)
### Instance Properties
- [var sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>](avplayeritemsamplebufferoutput/samplebufferinsequence/samplebuffer.md)
  Sample buffer containing media data.
- [var sequenceWasRestarted: Bool](avplayeritemsamplebufferoutput/samplebufferinsequence/sequencewasrestarted.md)
  Indicates the very first buffer in a new sequence produced by this output. Seeking or changing playback direction will start a new sequence of buffers. If you have any sample buffers queued from the previous sequence, these should be discarded.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextavailablesamplebuffer.md)
  Returns the next sample buffer if it is already available.
- [func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextsamplebuffer.md)
  Returns next sample buffer once it becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence)*