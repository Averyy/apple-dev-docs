# inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func inputPixelBufferReceiverRequestingMultiPass(for input: AVAssetWriterInput, pixelBufferAttributes attributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.PixelBufferReceiver, AVAssetWriterInput.MultiPassController)
```

#### Return Value

A tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

## Parameters

- `input`: The input to be attached to the writer.
- `attributes`: The attributes of pixel buffers that will be vended by the input provider’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputpixelbufferreceiverrequestingmultipass(for:pixelbufferattributes:))*