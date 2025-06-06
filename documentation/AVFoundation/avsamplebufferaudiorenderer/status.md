# status

**Framework**: AVFoundation  
**Kind**: property

The status of the audio renderer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

#### Discussion

A renderer begins with a status of [`AVQueuedSampleBufferRenderingStatus.unknown`](avqueuedsamplebufferrenderingstatus/unknown.md). As you add sample buffers to the queue for rendering, the renderer transitions to either [`AVQueuedSampleBufferRenderingStatus.rendering`](avqueuedsamplebufferrenderingstatus/rendering.md) or [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md).

If the status is `AVQueuedSampleBufferRenderingStatus.failed`, check the value of the renderer’s error property for information on the error encountered. This property is key value observable.

## See Also

- [enum AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md)
  The statuses for sample buffer rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/status)*