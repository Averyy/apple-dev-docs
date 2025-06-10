# inputCaptionReceiver(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns an input receiver for writing caption data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func inputCaptionReceiver(for input: AVAssetWriterInput) -> sending AVAssetWriterInput.CaptionReceiver
```

#### Return Value

A writer input receiver with an interface for writing caption data.

## Parameters

- `input`: The input to be attached to the writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputcaptionreceiver(for:))*