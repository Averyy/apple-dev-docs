# outputCaptionProvider(for:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns an output provider for reading caption groups.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func outputCaptionProvider(for output: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)? = nil) -> sending AVAssetReaderOutput.Provider<AVCaptionGroup>
```

#### Return Value

A reader output provider with an interface for reading caption groups.

## Parameters

- `output`: The output to be attached to the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputcaptionprovider(for:validationdelegate:))*