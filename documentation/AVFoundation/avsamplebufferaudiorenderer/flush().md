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
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush() method instead

## Declaration

```swift
func flush()
```

```objc
- (void) flush;
```

#### Discussion

Additional sample buffers can be appended after -flush.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/flush())*