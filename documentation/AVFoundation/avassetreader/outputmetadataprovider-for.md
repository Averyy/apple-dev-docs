# outputMetadataProvider(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns an output provider for reading timed metadata groups.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func outputMetadataProvider(for output: AVAssetReaderTrackOutput) -> sending AVAssetReaderOutput.Provider<AVTimedMetadataGroup>
```

#### Return Value

A reader output provider with an interface for reading timed metadata groups.

## Parameters

- `output`: The output to be attached to the reader.

## See Also

- [func outputProvider(for: AVAssetReaderOutput) -> sending AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>](avassetreader/outputprovider(for:).md)
  Attaches the output to the reader and returns an output provider for reading sample buffers.
- [func outputProviderWithRandomAccess(for: AVAssetReaderOutput) -> sending (AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputproviderwithrandomaccess(for:).md)
  Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [func outputCaptionProvider(for: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)?) -> sending AVAssetReaderOutput.Provider<AVCaptionGroup>](avassetreader/outputcaptionprovider(for:validationdelegate:).md)
  Attaches the output to the reader and returns an output provider for reading caption groups.
- [func outputCaptionProviderWithRandomAccess(for: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)?) -> sending (AVAssetReaderOutput.Provider<AVCaptionGroup>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputcaptionproviderwithrandomaccess(for:validationdelegate:).md)
  Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [func outputMetadataProviderWithRandomAccess(for: AVAssetReaderTrackOutput) -> sending (AVAssetReaderOutput.Provider<AVTimedMetadataGroup>, AVAssetReaderOutput.RandomAccessController)](avassetreader/outputmetadataproviderwithrandomaccess(for:).md)
  Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputmetadataprovider(for:))*