# AVSampleBufferAudioRendererFlushTimeKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

The key that indicates the presentation timestamp of the first queued sample that was flushed.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use the result of AVSampleBufferAudioRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithSuggestedFlushReason instead

## Declaration

```swift
let AVSampleBufferAudioRendererFlushTimeKey: String
```

```c
extern NSString * const AVSampleBufferAudioRendererFlushTimeKey;
```

## Discussion

The value for this key is an [`NSValue`](../Foundation/nsvalue.md) object that wraps a [`CMTime`](../CoreMedia/cmtime.md) value.

## See Also

### Removing queued buffers
- [func flush(fromSourceTime: CMTime, completionHandler: (Bool) -> Void)](./avsamplebufferaudiorenderer/flush%28fromsourcetime,completionhandler%29.md)
  Flushes queued sample buffers with presentation time stamps later than or equal to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorendererflushtimekey)*