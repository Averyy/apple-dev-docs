# inputPixelBufferReceiverRequestingMultiPass(for:pixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func inputPixelBufferReceiverRequestingMultiPass(for input: AVAssetWriterInput, pixelBufferAttributes attributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.PixelBufferReceiver, AVAssetWriterInput.MultiPassController)
```

#### Return Value

A tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.

## Parameters

- `input`: The input to be attached to the writer.
- `attributes`: The attributes of pixel buffers that will be vended by the input provider’s pixel buffer pool.

## See Also

- [func inputReceiver(for: AVAssetWriterInput) -> sending AVAssetWriterInput.SampleBufferReceiver](avassetwriter/inputreceiver(for:).md)
  Attaches the input to the writer and returns an input receiver for writing sample buffers.
- [func inputCaptionReceiver(for: AVAssetWriterInput) -> sending AVAssetWriterInput.CaptionReceiver](avassetwriter/inputcaptionreceiver(for:).md)
  Attaches the input to the writer and returns an input receiver for writing caption data.
- [func inputCaptionReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.CaptionReceiver, AVAssetWriterInput.MultiPassController)](avassetwriter/inputcaptionreceiverrequestingmultipass(for:).md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.
- [func inputMetadataReceiver(for: AVAssetWriterInput) -> sending AVAssetWriterInput.MetadataReceiver](avassetwriter/inputmetadatareceiver(for:).md)
  Attaches the input to the writer and returns an input receiver for writing timed metadata group.
- [func inputMetadataReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.MetadataReceiver, AVAssetWriterInput.MultiPassController)](avassetwriter/inputmetadatareceiverrequestingmultipass(for:).md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing timed metadata group, and an associated multi pass controller.
- [func inputPixelBufferReceiver(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending AVAssetWriterInput.PixelBufferReceiver](avassetwriter/inputpixelbufferreceiver(for:pixelbufferattributes:).md)
  Attaches the input to the writer and returns an input receiver for writing pixel buffers.
- [func inputReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.SampleBufferReceiver, AVAssetWriterInput.MultiPassController)](avassetwriter/inputreceiverrequestingmultipass(for:).md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.
- [func inputTaggedPixelBufferGroupReceiver(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending AVAssetWriterInput.TaggedPixelBufferGroupReceiver](avassetwriter/inputtaggedpixelbuffergroupreceiver(for:pixelbufferattributes:).md)
  Attaches the input to the writer and returns an input receiver for writing tagged pixel buffers.
- [func inputTaggedPixelBufferGroupReceiverRequestingMultiPass(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.TaggedPixelBufferGroupReceiver, AVAssetWriterInput.MultiPassController)](avassetwriter/inputtaggedpixelbuffergroupreceiverrequestingmultipass(for:pixelbufferattributes:).md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing tagged pixel buffers, and an associated multi pass controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputpixelbufferreceiverrequestingmultipass(for:pixelbufferattributes:))*