# error

**Framework**: AVFoundation  
**Kind**: property

An object the describes the error that caused the rendering failure.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

This value is `nil` by default. It only contains a valid error object when the [`status`](avsamplebuffervideorenderer/status.md) value is [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md).

## See Also

- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebuffervideorenderer/status.md)
  A status value that indicates whether this object can enqueue and render sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/error)*