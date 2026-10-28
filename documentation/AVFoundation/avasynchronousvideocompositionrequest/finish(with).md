# finish(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) finishWithError:(NSError *) error;
```

## Discussion

A custom compositor calls this method to indicate that the attempt to compose a frame failed.

## Parameters

- `error`: Returns the error encountered during the compositing.

## See Also

### Finishing the request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](./finish%28withcomposedvideoframe%29.md)
  Finishes the request to compose the frame.
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](./finish%28withcomposedpixelbuffer%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](./finish%28withcomposedtaggedbuffers%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finishCancelledRequest()](./finishcancelledrequest%28%29.md)
  Cancels the request to compose a video frame.
- [- finishWithComposedTaggedBufferGroup:](./finishwithcomposedtaggedbuffergroup_.md)
  The method that the custom compositor calls when composition succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(with:))*