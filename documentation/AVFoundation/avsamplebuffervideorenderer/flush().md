# flush()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Instructs the receiver to discard pending enqueued sample buffers.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush() method instead

## Declaration

```swift
func flush()
```

```objc
- (void) flush;
```

## Discussion

Additional sample buffers can be appended after -flush.

Video-specific notes:

It is not possible to determine which sample buffers have been decoded, so the next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/flush())*