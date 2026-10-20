# AVQueuedSampleBufferRenderingStatus.failed

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The object can no longer render sample buffers because of an error.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.2+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

## Declaration

```swift
case failed
```

```c
AVQueuedSampleBufferRenderingStatusFailed
```

## See Also

### Status values
- [AVQueuedSampleBufferRenderingStatus.unknown](./unknown.md)
  The object doesn’t have any sample buffers enqueued.
- [AVQueuedSampleBufferRenderingStatus.rendering](./rendering.md)
  The object is rendering the sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus/failed)*