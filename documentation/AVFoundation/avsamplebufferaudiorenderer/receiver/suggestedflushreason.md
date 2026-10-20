# AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Reasons the receiver suggests the client flush and re-enqueue.

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
enum SuggestedFlushReason
```

## Topics

### Flush reasons
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.outputConfigurationChanged](./suggestedflushreason/outputconfigurationchanged.md)
  The audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)](./suggestedflushreason/wasflushedautomatically%28at%29.md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Flushing the receiver
- [func flush()](./flush%28%29.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func flush(fromSourceTime: CMTime) async -> Bool](./flush%28fromsourcetime%29.md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason)*