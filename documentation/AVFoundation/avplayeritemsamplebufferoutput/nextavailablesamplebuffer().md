# nextAvailableSampleBuffer()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

## Discussion

If no sample buffers are ready, this method will return nil immediately.

This method will race with [`nextSampleBuffer()`](./nextsamplebuffer%28%29.md) for grabbing the generated sample buffer.

## See Also

### Retrieving sample buffers
- [func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](./nextsamplebuffer%28%29.md)
  Returns next sample buffer once it becomes available.
- [AVPlayerItemSampleBufferOutput.SampleBufferInSequence](./samplebufferinsequence.md)
  Holds the information necessary for processing generated sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/nextavailablesamplebuffer())*