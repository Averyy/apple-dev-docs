# nextAvailableSampleBuffer()

**Framework**: AVFoundation  
**Kind**: method

Returns the next sample buffer if it is already available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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