# finish(withComposedVideoFrame:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Finishes the request to compose the frame.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.9+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use finish(withComposedVideoFrame: CVReadOnlyPixelBuffer) instead

## Declaration

```swift
func finish(withComposedVideoFrame composedVideoFrame: CVPixelBuffer)
```

```objc
- (void) finishWithComposedVideoFrame:(CVPixelBufferRef) composedVideoFrame;
```

#### Discussion

A custom compositor calls this method to indicate that it’s composed a frame successfully.

## Parameters

- `composedVideoFrame`: The successfully composed pixel buffer.

## See Also

### Finishing the request
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](./finish%28withcomposedpixelbuffer%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](./finish%28withcomposedtaggedbuffers%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](./finish%28with%29.md)
  Finishes the request with an error.
- [func finishCancelledRequest()](./finishcancelledrequest%28%29.md)
  Cancels the request to compose a video frame.
- [- finishWithComposedTaggedBufferGroup:](./finishwithcomposedtaggedbuffergroup_.md)
  The method that the custom compositor calls when composition succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:))*