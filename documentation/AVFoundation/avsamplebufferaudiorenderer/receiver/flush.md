# flush()

**Framework**: AVFoundation  
**Kind**: method

Instructs the receiver to discard pending enqueued sample buffers.

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
func flush()
```

#### Discussion

Additional sample buffers can be appended after `flush()`.

## See Also

- [func flush(fromSourceTime: CMTime) async -> Bool](avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:).md)
  Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason](avsamplebufferaudiorenderer/receiver/suggestedflushreason.md)
  Reasons the receiver suggests the client flush and re-enqueue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush())*