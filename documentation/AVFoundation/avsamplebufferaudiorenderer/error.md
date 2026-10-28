# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The error that caused the renderer to no longer render sample buffers.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

## Discussion

The value of this property is nil unless the value of [`status`](./status.md) is [`AVQueuedSampleBufferRenderingStatus.failed`](../avqueuedsamplebufferrenderingstatus/failed.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/error)*