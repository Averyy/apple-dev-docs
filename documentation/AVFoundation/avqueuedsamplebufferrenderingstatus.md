# AVQueuedSampleBufferRenderingStatus

**Framework**: AVFoundation  
**Kind**: enum

The statuses for sample buffer rendering.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
enum AVQueuedSampleBufferRenderingStatus
```

## Topics

### Status Values
- [AVQueuedSampleBufferRenderingStatus.unknown](avqueuedsamplebufferrenderingstatus/unknown.md)
  The object doesn’t have any sample buffers enqueued.
- [AVQueuedSampleBufferRenderingStatus.rendering](avqueuedsamplebufferrenderingstatus/rendering.md)
  The object is rendering the sample buffer.
- [AVQueuedSampleBufferRenderingStatus.failed](avqueuedsamplebufferrenderingstatus/failed.md)
  The object can no longer render sample buffers because of an error.
### Initializers
- [init?(rawValue: Int)](avqueuedsamplebufferrenderingstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebufferaudiorenderer/status.md)
  The status of the audio renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus)*