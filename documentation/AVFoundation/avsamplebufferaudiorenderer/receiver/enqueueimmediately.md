# enqueueImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.

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
func enqueueImmediately(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult
```

#### Return Value

The result of the enqueue operation.

## Parameters

- `sampleBuffer`: The sample buffer to enqueue.

## See Also

- [func enqueue(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueue(_:).md)
  Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult](avsamplebufferaudiorenderer/receiver/enqueueresult.md)
  A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueimmediately(_:))*