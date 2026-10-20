# AVSampleBufferAudioRenderer.Receiver.RenderingEvent

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.

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
enum RenderingEvent
```

## Topics

### Rendering events
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged](./renderingevent/outputconfigurationchanged.md)
  Indicates that the audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](./renderingevent/wasflushedautomatically%28at%29.md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](./renderingevent/failed%28_%29.md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Observing rendering events
- [var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferAudioRenderer.Receiver.RenderingEvent, Never>](./renderingeventsafterfinishedenqueuing.md)
  A sequence of events that may occur when rendering after enqueuing samples has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent)*