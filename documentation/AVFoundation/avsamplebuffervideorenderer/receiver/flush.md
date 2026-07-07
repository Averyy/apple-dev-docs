# flush()

**Framework**: AVFoundation  
**Kind**: method

Instructs the receiver to discard pending enqueued sample buffers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func flush()
```

#### Discussion

Additional sample buffers can be appended after `flush()`.

> **Note**: For video, it is not possible to determine which sample buffers have been decoded, so the next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).

## See Also

- [func flush(removingDisplayedImage: Bool) async](avsamplebuffervideorenderer/receiver/flush(removingdisplayedimage:).md)
  Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush())*