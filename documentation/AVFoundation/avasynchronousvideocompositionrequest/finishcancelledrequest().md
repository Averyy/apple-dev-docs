# finishCancelledRequest()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels the request to compose a video frame.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func finishCancelledRequest()
```

```objc
- (void) finishCancelledRequest;
```

## See Also

### Finishing the request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](./finish%28withcomposedvideoframe%29.md)
  Finishes the request to compose the frame.
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](./finish%28withcomposedpixelbuffer%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](./finish%28withcomposedtaggedbuffers%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](./finish%28with%29.md)
  Finishes the request with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finishcancelledrequest())*