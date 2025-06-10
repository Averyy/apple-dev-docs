# inputCaptionReceiverRequestingMultiPass(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns a tuple with an input receiver for writing caption data, and an associated multi pass controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func inputCaptionReceiverRequestingMultiPass(for input: AVAssetWriterInput) -> sending (AVAssetWriterInput.CaptionReceiver, AVAssetWriterInput.MultiPassController)
```

#### Return Value

A tuple with an input receiver for writing caption data, and an associated multi pass controller.

## Parameters

- `input`: The input to be attached to the writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputcaptionreceiverrequestingmultipass(for:))*