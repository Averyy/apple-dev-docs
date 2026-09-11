# AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)

**Framework**: AVFoundation  
**Kind**: case

Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

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
case failed(any Error)
```

## See Also

- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged](avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged.md)
  Indicates that the audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](avsamplebufferaudiorenderer/receiver/renderingevent/wasflushedautomatically(at:).md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/failed(_:))*