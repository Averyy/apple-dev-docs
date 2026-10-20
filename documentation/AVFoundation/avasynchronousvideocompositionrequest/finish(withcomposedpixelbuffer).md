# finish(withComposedPixelBuffer:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

The method that the custom compositor calls when composition succeeds.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finish(withComposedPixelBuffer readOnlyPixelBuffer: CVReadOnlyPixelBuffer)
```

## See Also

### Finishing the request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](./finish%28withcomposedvideoframe%29.md)
  Finishes the request to compose the frame.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](./finish%28withcomposedtaggedbuffers%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](./finish%28with%29.md)
  Finishes the request with an error.
- [func finishCancelledRequest()](./finishcancelledrequest%28%29.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:))*