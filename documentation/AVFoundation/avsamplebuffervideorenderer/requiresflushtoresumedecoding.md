# requiresFlushToResumeDecoding

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var requiresFlushToResumeDecoding: Bool { get }
```

#### Discussion

When your app enters a state where using a video decoder resources is not permissible, the value of this property changes to [`true`](https://developer.apple.com/documentation/swift/true) along with the video renderer’s status changing to [`AVQueuedSampleBufferRenderingStatus.failed`](avqueuedsamplebufferrenderingstatus/failed.md). To resume rendering sample buffers, you must first reset the video renderer by calling [`flush()`](avqueuedsamplebufferrendering/flush().md) or [`flush(removingDisplayedImage:completionHandler:)`](avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:).md).

This property is not key-value observable. Instead, track changes to this property by observing notifications of type [`requiresFlushToResumeDecodingDidChangeNotification`](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md).

## See Also

- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:).md)
  Tells the video renderer to discard pending enqueued sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/requiresflushtoresumedecoding)*