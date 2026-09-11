# nextSampleBuffer()

**Framework**: AVFoundation  
**Kind**: method

Returns next sample buffer once it becomes available.

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
nonisolated
func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?
```

#### Discussion

This method will wait indefinitely for the next sample buffer to become available. This method returns nil if the current task is cancelled or if this method is called from a different task.

This method will race with [`nextAvailableSampleBuffer()`](avplayeritemsamplebufferoutput/nextavailablesamplebuffer().md) for grabbing the generated sample buffer.

## See Also

- [func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextavailablesamplebuffer.md)
  Returns the next sample buffer if it is already available.
- [AVPlayerItemSampleBufferOutput.SampleBufferInSequence](avplayeritemsamplebufferoutput/samplebufferinsequence.md)
  Holds the information necessary for processing generated sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/nextsamplebuffer())*