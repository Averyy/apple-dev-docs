# didFailToDecodeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification that indicates the video renderer fails to decode a sample buffer.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- tvOS 17.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithDecodeFailure instead

## Declaration

```swift
class let didFailToDecodeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVSampleBufferVideoRendererDidFailToDecodeNotification;
```

## See Also

### Handling decode failures
- [class let didFailToDecodeNotificationErrorKey: String](./didfailtodecodenotificationerrorkey.md)
  A key to retrieve an error object that provides the details of the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/didfailtodecodenotification)*