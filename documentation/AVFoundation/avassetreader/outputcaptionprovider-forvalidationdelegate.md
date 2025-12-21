# outputCaptionProvider(for:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns an output provider for reading caption groups.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
func outputCaptionProvider(for output: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)? = nil) -> sending AVAssetReaderOutput.Provider<AVCaptionGroup>
```

#### Return Value

A reader output provider with an interface for reading caption groups.

## Parameters

- `output`: The output to be attached to the reader.

## See Also

- [func outputProvider(for: AVAssetReaderOutput) -> sending AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>](avassetreader/outputprovider(for:).md)
  Attaches the output to the reader and returns an output provider for reading sample buffers.
- [func outputProviderWithRandomAccess(for: AVAssetReaderOutput) -> sending (AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputproviderwithrandomaccess(for:).md)
  Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [func outputCaptionProviderWithRandomAccess(for: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)?) -> sending (AVAssetReaderOutput.Provider<AVCaptionGroup>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputcaptionproviderwithrandomaccess(for:validationdelegate:).md)
  Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [func outputMetadataProvider(for: AVAssetReaderTrackOutput) -> sending AVAssetReaderOutput.Provider<AVTimedMetadataGroup>](avassetreader/outputmetadataprovider(for:).md)
  Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [func outputMetadataProviderWithRandomAccess(for: AVAssetReaderTrackOutput) -> sending (AVAssetReaderOutput.Provider<AVTimedMetadataGroup>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputmetadataproviderwithrandomaccess(for:).md)
  Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputcaptionprovider(for:validationdelegate:))*