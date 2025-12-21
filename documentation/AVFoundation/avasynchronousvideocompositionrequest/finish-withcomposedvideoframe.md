# finish(withComposedVideoFrame:)

**Framework**: AVFoundation  
**Kind**: method

Finishes the request to compose the frame.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finish(withComposedVideoFrame composedVideoFrame: CVPixelBuffer)
```

#### Discussion

A custom compositor calls this method to indicate that it’s composed a frame successfully.

## Parameters

- `composedVideoFrame`: The successfully composed pixel buffer.

## See Also

- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:).md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:).md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](avasynchronousvideocompositionrequest/finish(with:).md)
  Finishes the request with an error.
- [func finishCancelledRequest()](avasynchronousvideocompositionrequest/finishcancelledrequest.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:))*