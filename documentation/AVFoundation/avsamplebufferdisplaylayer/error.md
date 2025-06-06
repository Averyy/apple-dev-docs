# error

**Framework**: AVFoundation  
**Kind**: property

The error that caused the failure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The value of this property is an `NSError` that describes what caused the display layer to no longer be able to enqueue sample buffers. If the status is not [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md), the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/error)*