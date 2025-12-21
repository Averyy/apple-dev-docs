# finish(withComposedPixelBuffer:)

**Framework**: AVFoundation  
**Kind**: method

The method that the custom compositor calls when composition succeeds.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finish(withComposedPixelBuffer readOnlyPixelBuffer: CVReadOnlyPixelBuffer)
```

## See Also

- [func finish(withComposedVideoFrame: CVPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md)
  Finishes the request to compose the frame.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:).md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](avasynchronousvideocompositionrequest/finish(with:).md)
  Finishes the request with an error.
- [func finishCancelledRequest()](avasynchronousvideocompositionrequest/finishcancelledrequest.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:))*