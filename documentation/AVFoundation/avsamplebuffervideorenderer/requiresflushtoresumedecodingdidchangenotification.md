# requiresFlushToResumeDecodingDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- tvOS 17.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .requiresFlushToResumeDecoding instead

## Declaration

```swift
class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification;
```

## See Also

### Flushing the renderer
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md)
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](./flush%28removingdisplayedimage,completionhandler%29.md)
  Tells the video renderer to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification)*