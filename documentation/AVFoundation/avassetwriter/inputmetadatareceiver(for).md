# inputMetadataReceiver(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Attaches the input to the writer and returns an input receiver for writing timed metadata group.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func inputMetadataReceiver(for input: AVAssetWriterInput) -> sending AVAssetWriterInput.MetadataReceiver
```

## Return Value

A writer input receiver with an interface for writing timed metadata group.

## Parameters

- `input`: The input to be attached to the writer.

## See Also

### Configuring input receivers
- [func inputReceiver(for: AVAssetWriterInput) -> sending AVAssetWriterInput.SampleBufferReceiver](./inputreceiver%28for%29.md)
  Attaches the input to the writer and returns an input receiver for writing sample buffers.
- [func inputCaptionReceiver(for: AVAssetWriterInput) -> sending AVAssetWriterInput.CaptionReceiver](./inputcaptionreceiver%28for%29.md)
  Attaches the input to the writer and returns an input receiver for writing caption data.
- [func inputCaptionReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.CaptionReceiver, AVAssetWriterInput.MultiPassController)](./inputcaptionreceiverrequestingmultipass%28for%29.md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.
- [func inputMetadataReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.MetadataReceiver, AVAssetWriterInput.MultiPassController)](./inputmetadatareceiverrequestingmultipass%28for%29.md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing timed metadata group, and an associated multi pass controller.
- [func inputPixelBufferReceiver(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending AVAssetWriterInput.PixelBufferReceiver](./inputpixelbufferreceiver%28for,pixelbufferattributes%29.md)
  Attaches the input to the writer and returns an input receiver for writing pixel buffers.
- [func inputPixelBufferReceiverRequestingMultiPass(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.PixelBufferReceiver, AVAssetWriterInput.MultiPassController)](./inputpixelbufferreceiverrequestingmultipass%28for,pixelbufferattributes%29.md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing pixel buffers, and an associated multi pass controller.
- [func inputReceiverRequestingMultiPass(for: AVAssetWriterInput) -> sending (AVAssetWriterInput.SampleBufferReceiver, AVAssetWriterInput.MultiPassController)](./inputreceiverrequestingmultipass%28for%29.md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.
- [func inputTaggedPixelBufferGroupReceiver(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending AVAssetWriterInput.TaggedPixelBufferGroupReceiver](./inputtaggedpixelbuffergroupreceiver%28for,pixelbufferattributes%29.md)
  Attaches the input to the writer and returns an input receiver for writing tagged pixel buffers.
- [func inputTaggedPixelBufferGroupReceiverRequestingMultiPass(for: AVAssetWriterInput, pixelBufferAttributes: CVPixelBufferCreationAttributes?) -> sending (AVAssetWriterInput.TaggedPixelBufferGroupReceiver, AVAssetWriterInput.MultiPassController)](./inputtaggedpixelbuffergroupreceiverrequestingmultipass%28for,pixelbufferattributes%29.md)
  Attaches the input to the writer and returns a tuple with an input receiver for writing tagged pixel buffers, and an associated multi pass controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputmetadatareceiver(for:))*