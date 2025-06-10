# outputCaptionProviderWithRandomAccess(for:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func outputCaptionProviderWithRandomAccess(for output: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)? = nil) -> sending (AVAssetReaderOutput.Provider<AVCaptionGroup>, AVAssetReaderOutput.RandomAccessController)
```

#### Return Value

A tuple with an output provider for reading caption groups, and an associated random access controller.

## Parameters

- `output`: The output to be attached to the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputcaptionproviderwithrandomaccess(for:validationdelegate:))*