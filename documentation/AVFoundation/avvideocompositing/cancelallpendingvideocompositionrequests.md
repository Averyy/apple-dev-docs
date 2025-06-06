# cancelAllPendingVideoCompositionRequests()

**Framework**: AVFoundation  
**Kind**: method

Directs a custom video compositor object to cancel or finish all pending video composition requests.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func cancelAllPendingVideoCompositionRequests()
```

#### Discussion

Upon receiving this message, a custom video compositor must block until it has either cancelled all pending frame requests, and called the [`finishCancelledRequest()`](avasynchronousvideocompositionrequest/finishcancelledrequest().md) method for each of them. If cancellation is not possible, the method must block until it has finished processing of all the frames and called the [`finish(withComposedVideoFrame:)`](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md) method for each of them.

## See Also

- [func startRequest(AVAsynchronousVideoCompositionRequest)](avvideocompositing/startrequest(_:).md)
  Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [class AVAsynchronousVideoCompositionRequest](avasynchronousvideocompositionrequest.md)
  An object that contains information a video compositor needs to render an output pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/cancelallpendingvideocompositionrequests())*