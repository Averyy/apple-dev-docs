# flush(removingDisplayedImage:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the video renderer to discard pending enqueued sample buffers.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- tvOS 17.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush(removingDisplayedImage:) method instead

## Declaration

```swift
func flush(removingDisplayedImage removeDisplayedImage: Bool, completionHandler handler: (@Sendable () -> Void)? = nil)
```

```swift
func flush(removingDisplayedImage removeDisplayedImage: Bool) async
```

```objc
- (void) flushWithRemovalOfDisplayedImage:(BOOL) removeDisplayedImage completionHandler:(void (^)()) handler;
```

## Parameters

- `removeDisplayedImage`: A Boolean value that indicates whether to remove the display image.
- `handler`: A completion handler the system invokes when the flush completes.

## See Also

### Flushing the renderer
- [var requiresFlushToResumeDecoding: Bool](./requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](./requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String](../avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:))*