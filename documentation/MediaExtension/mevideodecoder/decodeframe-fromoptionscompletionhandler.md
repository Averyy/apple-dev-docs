# decodeFrame(from:options:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Requests the extension to decode a video frame.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func decodeFrame(from sampleBuffer: CMSampleBuffer, options: MEDecodeFrameOptions) async throws -> (CVImageBuffer, MEDecodeFrameStatus)
```

#### Discussion

This method calls the completion handler for every sample buffer frame when decoding completes, but not necessarily in display order. The completion handler receives a decoded pixel buffer, a decode status that indicates a frame dropped, or an error. Use [`MEVideoDecoderPixelBufferManager`](mevideodecoderpixelbuffermanager.md) to allocate an image buffer. If an error occurs that’s external to [`MediaExtensionErrorDomain`](mediaextensionerrordomain.md), the [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession) receives it as [`kVTVideoDecoderUnknownErr`](https://developer.apple.com/documentation/VideoToolbox/kVTVideoDecoderUnknownErr).

## Parameters

- `sampleBuffer`: A sample buffer that contains one video frame.
- `options`: Specific decode options for the frame.
- `completionHandler`: The completion block to execute when the decode operation finishes.

## See Also

- [func canAccept(CMFormatDescription) -> Bool](mevideodecoder/canaccept(_:).md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [struct MEDecodeFrameStatus](medecodeframestatus.md)
  A type that represents a non-error status related to a frame decode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/decodeframe(from:options:completionhandler:))*