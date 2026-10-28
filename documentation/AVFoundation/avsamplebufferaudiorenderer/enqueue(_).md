# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sends a sample buffer in order to render its contents.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's enqueue(_:) async or enqueueImmediately(_:) methods instead

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

```objc
- (void) enqueueSampleBuffer:(CMSampleBufferRef) sampleBuffer;
```

## Discussion

The audio in the sample buffer is rendered at the sample buffer’s output presentation timestamp, as interpreted by the timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/enqueue(_:))*