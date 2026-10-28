# flush()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Discards all pending enqueued sample buffers.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

## Declaration

```swift
func flush()
```

```objc
- (void) flush;
```

## Discussion

It is not possible to determine which sample buffers have been decoded for video. The next frame passed to [`enqueue(_:)`](./enqueue%28_%29.md) should be an IDR frame (also known as a key frame or sync sample).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/flush())*