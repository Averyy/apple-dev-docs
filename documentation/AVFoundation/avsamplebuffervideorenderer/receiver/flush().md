# flush()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Instructs the receiver to discard pending enqueued sample buffers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func flush()
```

## Discussion

Additional sample buffers can be appended after `flush()`.

> **Note**: For video, it is not possible to determine which sample buffers have been decoded, so the next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing the receiver
- [func flush(removingDisplayedImage: Bool) async](./flush%28removingdisplayedimage%29.md)
  Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush())*