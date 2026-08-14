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

### Status values
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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebufferaudiorenderer/status.md)
  The status of the audio renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus)*