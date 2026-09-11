# AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged

**Framework**: AVFoundation  
**Kind**: case

Indicates that the audio output configuration has changed.

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
case outputConfigurationChanged
```

## See Also

- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](avsamplebufferaudiorenderer/receiver/renderingevent/wasflushedautomatically(at:).md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](avsamplebufferaudiorenderer/receiver/renderingevent/failed(_:).md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged)*