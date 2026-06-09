# AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason

**Framework**: AVFoundation  
**Kind**: enum

Reasons the receiver suggests the client flush and re-enqueue.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum SuggestedFlushReason
```

## Topics

### Flush reasons
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.outputConfigurationChanged](avsamplebufferaudiorenderer/receiver/suggestedflushreason/outputconfigurationchanged.md)
  The audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)](avsamplebufferaudiorenderer/receiver/suggestedflushreason/wasflushedautomatically(at:).md)
  The enqueued media data has been flushed for a reason other than a call to the `flush()` method.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func flush()](avsamplebufferaudiorenderer/receiver/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func flush(fromSourceTime: CMTime) async -> Bool](avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:).md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason)*