# AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 27.0+ - Deprecated in 27.0
- iPadOS 27.0+ - Deprecated in 27.0
- Mac Catalyst 27.0+ - Deprecated in 27.0
- macOS 27.0+ - Deprecated in 27.0
- tvOS 27.0+ - Deprecated in 27.0
- visionOS 27.0+ - Deprecated in 27.0

> **Deprecated**: Use the result of AVSampleBufferVideoRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .requiresFlushToResumeDecoding instead

## Declaration

```swift
let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String
```

```c
extern NSString * const AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey;
```

## See Also

### Flushing the renderer
- [var requiresFlushToResumeDecoding: Bool](./avsamplebuffervideorenderer/requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](./avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](./avsamplebuffervideorenderer/flush%28removingdisplayedimage,completionhandler%29.md)
  Tells the video renderer to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey)*