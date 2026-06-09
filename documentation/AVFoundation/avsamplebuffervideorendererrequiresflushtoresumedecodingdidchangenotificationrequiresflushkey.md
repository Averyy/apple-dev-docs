# AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey

**Framework**: AVFoundation  
**Kind**: var

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String
```

## See Also

- [var requiresFlushToResumeDecoding: Bool](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:).md)
  Tells the video renderer to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey)*