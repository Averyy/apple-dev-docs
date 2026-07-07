# renderingEventsAfterFinishedEnqueuing

**Framework**: AVFoundation  
**Kind**: property

A sequence of events that may occur when rendering after enqueuing samples has finished.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferAudioRenderer.Receiver.RenderingEvent, Never> { get }
```

#### Discussion

After enqueuing samples, iterate over this sequence to discover any issues that may occur while the renderer continues rendering. Break out of the iteration when done monitoring rendering events.

## See Also

- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent](avsamplebufferaudiorenderer/receiver/renderingevent.md)
  Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingeventsafterfinishedenqueuing)*