# inputPixelBufferReceiver(for:pixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns an input receiver for writing pixel buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func inputPixelBufferReceiver(for input: AVAssetWriterInput, pixelBufferAttributes attributes: CVPixelBufferCreationAttributes?) -> sending AVAssetWriterInput.PixelBufferReceiver
```

#### Return Value

A writer input receiver with an interface for writing pixel buffers.

## Parameters

- `input`: The input to be attached to the writer.
- `attributes`: The attributes of pixel buffers that will be vended by the input provider’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputpixelbufferreceiver(for:pixelbufferattributes:))*