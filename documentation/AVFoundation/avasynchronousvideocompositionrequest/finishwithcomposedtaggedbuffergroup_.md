# finishWithComposedTaggedBufferGroup:

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

```objc
- (void) finishWithComposedTaggedBufferGroup:(CMTaggedBufferGroupRef) taggedBufferGroup;
```

## Parameters

- `taggedBufferGroup`: The tagged buffer group containing the composed tagged buffers. The tagged buffers must be compatible with the outputBufferDescription specified in the video composition. The outputBufferDescription must not be nil when calling this function. NOTE: If `AVVideoComposition/spatialConfigurations` is not empty, then `attach(spatialVideoConfiguration:to:)` must be called with one of the spatial configurations. An exception will be thrown otherwise. Also, all pixel buffers must be associated with the same spatial configuration. An exception will be thrown otherwise.

## See Also

### Finishing the request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](./finish%28withcomposedvideoframe%29.md)
  Finishes the request to compose the frame.
- [func finish(with: any Error)](./finish%28with%29.md)
  Finishes the request with an error.
- [func finishCancelledRequest()](./finishcancelledrequest%28%29.md)
  Cancels the request to compose a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finishwithcomposedtaggedbuffergroup:)*