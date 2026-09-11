# nextAvailableSampleBuffer()

**Framework**: AVFoundation  
**Kind**: method

Returns the next sample buffer if it is already available.

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
func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?
```

#### Discussion

If no sample buffers are ready, this method will return nil immediately.

This method will race with [`nextSampleBuffer()`](avplayeritemsamplebufferoutput/nextsamplebuffer().md) for grabbing the generated sample buffer.

## See Also

- [func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextsamplebuffer.md)
  Returns next sample buffer once it becomes available.
- [AVPlayerItemSampleBufferOutput.SampleBufferInSequence](avplayeritemsamplebufferoutput/samplebufferinsequence.md)
  Holds the information necessary for processing generated sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/nextavailablesamplebuffer())*