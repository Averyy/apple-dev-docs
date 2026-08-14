# AVSampleBufferVideoRenderer.Receiver.RenderingEvent

**Framework**: AVFoundation  
**Kind**: enum

Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum RenderingEvent
```

## Topics

### Rendering events
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)](avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:).md)
  Indicates that the renderer failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)](avsamplebuffervideorenderer/receiver/renderingevent/requiresflushtoresumedecoding(_:).md)
  The Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)](avsamplebuffervideorenderer/receiver/renderingevent/failed(_:).md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferVideoRenderer.Receiver.RenderingEvent, Never>](avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent)*