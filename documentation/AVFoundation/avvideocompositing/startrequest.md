# startRequest(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest)
```

#### Discussion

The custom compositor is expected to invoke, either subsequently or immediately,  the `asyncVideoCompositionRequest` object’s [`finish(withComposedVideoFrame:)`](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md) or [`finish(with:)`](avasynchronousvideocompositionrequest/finish(with:).md) methods.

If you intend to finish rendering the frame after  handling of this message returns, you must retain `asyncVideoCompositionRequest` until after composition is finished.

Note that if the custom compositor’s implementation of this method returns without finishing the composition immediately, it may be invoked again with another composition request before the prior request is finished; in such cases the custom compositor should be prepared to manage multiple composition requests.

If the rendered frame is exactly the same as one of the source frames, with no letterboxing, pillboxing or cropping needed, then the appropriate source pixel buffer may be returned, after [`CFRetain`](https://developer.apple.com/documentation/corefoundation/1521269-cfretain) has been called on it).

## Parameters

- `asyncVideoCompositionRequest`: An instance of   that provides context for the requested composition.

## See Also

- [class AVAsynchronousVideoCompositionRequest](avasynchronousvideocompositionrequest.md)
  An object that contains information a video compositor needs to render an output pixel buffer.
- [func cancelAllPendingVideoCompositionRequests()](avvideocompositing/cancelallpendingvideocompositionrequests.md)
  Directs a custom video compositor object to cancel or finish all pending video composition requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/startrequest(_:))*