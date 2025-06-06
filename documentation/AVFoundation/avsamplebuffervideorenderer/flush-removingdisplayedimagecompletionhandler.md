# flush(removingDisplayedImage:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Tells the video renderer to discard pending enqueued sample buffers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func flush(removingDisplayedImage removeDisplayedImage: Bool) async
```

## Parameters

- `removeDisplayedImage`: A Boolean value that indicates whether to remove the display image.
- `handler`: A completion handler the system invokes when the flush completes.

## See Also

- [var requiresFlushToResumeDecoding: Bool](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:))*