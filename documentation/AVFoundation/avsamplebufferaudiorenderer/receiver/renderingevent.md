# AVSampleBufferAudioRenderer.Receiver.RenderingEvent

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
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum RenderingEvent
```

## Topics

### Rendering events
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged](avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged.md)
  Indicates that the audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](avsamplebufferaudiorenderer/receiver/renderingevent/wasflushedautomatically(at:).md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](avsamplebufferaudiorenderer/receiver/renderingevent/failed(_:).md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferAudioRenderer.Receiver.RenderingEvent, Never>](avsamplebufferaudiorenderer/receiver/renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent)*