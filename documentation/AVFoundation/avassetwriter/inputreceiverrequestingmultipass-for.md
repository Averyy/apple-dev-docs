# inputReceiverRequestingMultiPass(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns a tuple with an input receiver for writing sample buffers, and an associated multi pass controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func inputReceiverRequestingMultiPass(for input: AVAssetWriterInput) -> sending (AVAssetWriterInput.SampleBufferReceiver, AVAssetWriterInput.MultiPassController)
```

#### Return Value

A tuple with an input receiver for writing sample buffers, and an associated multi pass controller.

## Parameters

- `input`: The input to be attached to the writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputreceiverrequestingmultipass(for:))*