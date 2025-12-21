# finish(withComposedTaggedBuffers:)

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
func finish(withComposedTaggedBuffers taggedBuffers: [CMTaggedDynamicBuffer])
```

## Parameters

- `taggedBuffers`: The tagged buffers containing the composed tagged buffers. The tagged buffers must be compatible with the outputBufferDescription specified in the video composition. The outputBufferDescription must not be nil when calling this function.   NOTE: If   is not empty, then   must be called with one of the spatial configurations. An exception will be thrown otherwise. Also, all pixel buffers must be associated with the same spatial configuration. An exception will be thrown otherwise.

## See Also

- [func finish(withComposedVideoFrame: CVPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md)
  Finishes the request to compose the frame.
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:).md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](avasynchronousvideocompositionrequest/finish(with:).md)
  Finishes the request with an error.
- [func finishCancelledRequest()](avasynchronousvideocompositionrequest/finishcancelledrequest.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:))*