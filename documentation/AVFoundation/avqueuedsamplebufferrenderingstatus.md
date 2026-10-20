# AVQueuedSampleBufferRenderingStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

The statuses for sample buffer rendering.

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
enum AVQueuedSampleBufferRenderingStatus
```

```c
enum AVQueuedSampleBufferRenderingStatus : NSInteger;
```

## Topics

### Status values
- [AVQueuedSampleBufferRenderingStatus.unknown](./avqueuedsamplebufferrenderingstatus/unknown.md)
  The object doesn’t have any sample buffers enqueued.
- [AVQueuedSampleBufferRenderingStatus.rendering](./avqueuedsamplebufferrenderingstatus/rendering.md)
  The object is rendering the sample buffer.
- [AVQueuedSampleBufferRenderingStatus.failed](./avqueuedsamplebufferrenderingstatus/failed.md)
  The object can no longer render sample buffers because of an error.
### Initializers
- [init?(rawValue: Int)](./avqueuedsamplebufferrenderingstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining rendering status
- [var status: AVQueuedSampleBufferRenderingStatus](./avsamplebufferaudiorenderer/status.md)
  The status of the audio renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus)*