# decodeFrame(from:options:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests the extension to decode a video frame.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func decodeFrame(from sampleBuffer: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: @escaping @Sendable (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)
```

```swift
func decodeFrame(from sampleBuffer: CMSampleBuffer, options: MEDecodeFrameOptions) async throws -> (CVImageBuffer, MEDecodeFrameStatus)
```

```objc
- (void) decodeFrameFromSampleBuffer:(CMSampleBufferRef) sampleBuffer options:(MEDecodeFrameOptions *) options completionHandler:(void (^)(CVImageBufferRef imageBuffer, MEDecodeFrameStatus decodeStatus, NSError *error)) completionHandler;
```

## Discussion

This method calls the completion handler for every sample buffer frame when decoding completes, but not necessarily in display order. The completion handler receives a decoded pixel buffer, a decode status that indicates a frame dropped, or an error. Use [`MEVideoDecoderPixelBufferManager`](../mevideodecoderpixelbuffermanager.md) to allocate an image buffer. If an error occurs that’s external to [`MediaExtensionErrorDomain`](../mediaextensionerrordomain.md), the [`VTDecompressionSession`](../../VideoToolbox/vtdecompressionsession.md) receives it as [`kVTVideoDecoderUnknownErr`](../../VideoToolbox/kvtvideodecoderunknownerr.md).

## Parameters

- `sampleBuffer`: A sample buffer that contains one video frame.
- `options`: Specific decode options for the frame.
- `completionHandler`: The completion block to execute when the decode operation finishes.

## See Also

### Decoding frames
- [func canAccept(CMFormatDescription) -> Bool](./canaccept%28_%29.md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [struct MEDecodeFrameStatus](../medecodeframestatus.md)
  A type that represents a non-error status related to a frame decode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/decodeframe(from:options:completionhandler:))*