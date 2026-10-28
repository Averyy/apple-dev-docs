# flush()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Instructs the receiver to discard pending enqueued sample buffers.

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
func flush()
```

## Discussion

Additional sample buffers can be appended after `flush()`.

## See Also

### Flushing the receiver
- [func flush(fromSourceTime: CMTime) async -> Bool](./flush%28fromsourcetime%29.md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason](./suggestedflushreason.md)
  Reasons the receiver suggests the client flush and re-enqueue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush())*