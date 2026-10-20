# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The error that caused the failure.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.10+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`error`](../avsamplebuffervideorenderer/error.md) on [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

#### Discussion

The value of this property is an `NSError` that describes what caused the display layer to no longer be able to enqueue sample buffers. If the status is not [`AVQueuedSampleBufferRenderingStatus.failed`](../avqueuedsamplebufferrenderingstatus/failed.md), the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/error)*