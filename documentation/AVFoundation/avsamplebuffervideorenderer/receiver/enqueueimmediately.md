# enqueueImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func enqueueImmediately(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult
```

#### Return Value

The result of the enqueue operation.

## Parameters

- `sampleBuffer`: The sample buffer to enqueue.

## See Also

- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult](avsamplebuffervideorenderer/receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueimmediately(_:))*