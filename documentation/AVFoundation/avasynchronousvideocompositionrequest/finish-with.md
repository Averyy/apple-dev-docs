# finish(with:)

**Framework**: AVFoundation  
**Kind**: method

Finishes the request with an error.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finish(with error: any Error)
```

#### Discussion

A custom compositor calls this method to indicate that the attempt to compose a frame failed.

## Parameters

- `error`: Returns the error encountered during the compositing.

## See Also

- [func finish(withComposedVideoFrame: CVPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md)
  Finishes the request to compose the frame.
- [func finishCancelledRequest()](avasynchronousvideocompositionrequest/finishcancelledrequest.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(with:))*