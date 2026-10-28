# requiresFlushToResumeDecoding

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.

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
var requiresFlushToResumeDecoding: Bool { get }
```

```objc
@property (readonly) BOOL requiresFlushToResumeDecoding;
```

## Discussion

When your app enters a state where using a video decoder resources is not permissible, the value of this property changes to [`true`](../../Swift/true.md) along with the video renderer’s status changing to [`AVQueuedSampleBufferRenderingStatus.failed`](../avqueuedsamplebufferrenderingstatus/failed.md). To resume rendering sample buffers, you must first reset the video renderer by calling [`flush()`](../avqueuedsamplebufferrendering/flush%28%29.md) or [`flush(removingDisplayedImage:completionHandler:)`](./flush%28removingdisplayedimage,completionhandler%29.md).

This property is not key-value observable. Instead, track changes to this property by observing notifications of type [`requiresFlushToResumeDecodingDidChangeNotification`](./requiresflushtoresumedecodingdidchangenotification.md).

## See Also

### Flushing the renderer
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](./requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md)
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](./flush%28removingdisplayedimage,completionhandler%29.md)
  Tells the video renderer to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecoding)*