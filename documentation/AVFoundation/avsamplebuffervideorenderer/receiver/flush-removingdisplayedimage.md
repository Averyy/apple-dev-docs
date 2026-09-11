# flush(removingDisplayedImage:)

**Framework**: AVFoundation  
**Kind**: method

Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) func flush(removingDisplayedImage removeDisplayedImage: Bool) async
```

#### Discussion

A flush resets decoder state. The next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).

## Parameters

- `removeDisplayedImage`: Set to true to remove any currently displayed image, false to preserve any current image.

## See Also

- [func flush()](avsamplebuffervideorenderer/receiver/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush(removingdisplayedimage:))*