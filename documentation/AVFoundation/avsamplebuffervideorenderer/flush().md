# flush()

**Framework**: AVFoundation  
**Kind**: method

Instructs the receiver to discard pending enqueued sample buffers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func flush()
```

#### Discussion

Additional sample buffers can be appended after -flush.

Video-specific notes:

It is not possible to determine which sample buffers have been decoded, so the next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/flush())*