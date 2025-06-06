# AVSampleBufferAudioRendererFlushTimeKey

**Framework**: AVFoundation  
**Kind**: var

The key that indicates the presentation timestamp of the first queued sample that was flushed.

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
let AVSampleBufferAudioRendererFlushTimeKey: String
```

#### Discussion

The value for this key is an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object that wraps a [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) value.

## See Also

- [func flush(fromSourceTime: CMTime, completionHandler: (Bool) -> Void)](avsamplebufferaudiorenderer/flush(fromsourcetime:completionhandler:).md)
  Flushes queued sample buffers with presentation time stamps later than or equal to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorendererflushtimekey)*