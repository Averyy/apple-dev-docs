# renderingEventsAfterFinishedEnqueuing

**Framework**: AVFoundation  
**Kind**: property

A sequence of events that may occur when rendering after enqueuing samples has finished.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferVideoRenderer.Receiver.RenderingEvent, Never> { get }
```

#### Discussion

After enqueuing samples, iterate over this sequence to discover any issues that may occur while the renderer continues rendering. Break out of the iteration when done monitoring rendering events.

## See Also

- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent](avsamplebuffervideorenderer/receiver/renderingevent.md)
  Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing)*