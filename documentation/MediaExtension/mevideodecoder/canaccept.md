# canAccept(_:)

**Framework**: MediaExtension  
**Kind**: method

Asks the extension whether the decoder can decode frames with the format description that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func canAccept(_ formatDescription: CMFormatDescription) -> Bool
```

## Parameters

- `formatDescription`: The new format description to evaluate.

## See Also

- [func decodeFrame(from: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)](mevideodecoder/decodeframe(from:options:completionhandler:).md)
  Requests the extension to decode a video frame.
- [struct MEDecodeFrameStatus](medecodeframestatus.md)
  A type that represents a non-error status related to a frame decode operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder/canaccept(_:))*