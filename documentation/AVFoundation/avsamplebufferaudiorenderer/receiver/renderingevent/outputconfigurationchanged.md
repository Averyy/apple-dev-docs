# AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

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

### Rendering events
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](./wasflushedautomatically%28at%29.md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](./failed%28_%29.md)
  Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged)*