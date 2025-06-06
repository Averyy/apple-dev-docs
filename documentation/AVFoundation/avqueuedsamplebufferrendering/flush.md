# flush()

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Discards all pending enqueued sample buffers.

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
func flush()
```

#### Discussion

It is not possible to determine which sample buffers have been decoded for video. The next frame passed to [`enqueue(_:)`](avqueuedsamplebufferrendering/enqueue(_:).md) should be an IDR frame (also known as a key frame or sync sample).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/flush())*