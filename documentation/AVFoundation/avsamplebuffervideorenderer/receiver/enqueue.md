# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func enqueue(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult
```

#### Return Value

The result of the enqueue operation.

#### Discussion

> **Note**: `CancellationError` if the Task was cancelled.

## Parameters

- `sampleBuffer`: The sample buffer to enqueue.

## See Also

- [func enqueueImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueimmediately(_:).md)
  Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueue(_:))*