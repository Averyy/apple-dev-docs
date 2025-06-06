# status

**Framework**: AVFoundation  
**Kind**: property

The ability of the display layer to be used for enqueuing sample buffers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`status`](avsamplebuffervideorenderer/status.md) on [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

The value of this property is an [`AVQueuedSampleBufferRenderingStatus`](avqueuedsamplebufferrenderingstatus.md) that indicates whether the receiver can be used for enqueuing sample buffers.

When the value of this property is [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md), the receiver can no longer be used and a new instance needs to be created in its place. When this happens, clients can check the value of the [`error`](avsamplebufferdisplaylayer/error.md) property to determine the failure.

This property supports key-value observing.

## See Also

- [enum AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md)
  The statuses for sample buffer rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/status)*