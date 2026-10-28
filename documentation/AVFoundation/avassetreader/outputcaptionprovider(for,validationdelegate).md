# outputCaptionProvider(for:validationDelegate:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Attaches the output to the reader and returns an output provider for reading caption groups.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func outputCaptionProvider(for output: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)? = nil) -> sending AVAssetReaderOutput.Provider<AVCaptionGroup>
```

## Return Value

A reader output provider with an interface for reading caption groups.

## Parameters

- `output`: The output to be attached to the reader.

## See Also

### Accessing output providers
- [func outputProvider(for: AVAssetReaderOutput) -> sending AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>](./outputprovider%28for%29.md)
  Attaches the output to the reader and returns an output provider for reading sample buffers.
- [func outputProviderWithRandomAccess(for: AVAssetReaderOutput) -> sending (AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>, AVAssetReaderOutput.RandomAccessController)](./outputproviderwithrandomaccess%28for%29.md)
  Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.
- [func outputCaptionProviderWithRandomAccess(for: AVAssetReaderTrackOutput, validationDelegate: (any AVAssetReaderCaptionValidationHandling)?) -> sending (AVAssetReaderOutput.Provider<AVCaptionGroup>, AVAssetReaderOutput.RandomAccessController)](./outputcaptionproviderwithrandomaccess%28for,validationdelegate%29.md)
  Attaches the output to the reader and returns a tuple with an output provider for reading caption groups, and an associated random access controller.
- [func outputMetadataProvider(for: AVAssetReaderTrackOutput) -> sending AVAssetReaderOutput.Provider<AVTimedMetadataGroup>](./outputmetadataprovider%28for%29.md)
  Attaches the output to the reader and returns an output provider for reading timed metadata groups.
- [func outputMetadataProviderWithRandomAccess(for: AVAssetReaderTrackOutput) -> sending (AVAssetReaderOutput.Provider<AVTimedMetadataGroup>, AVAssetReaderOutput.RandomAccessController)](./outputmetadataproviderwithrandomaccess%28for%29.md)
  Attaches the output to the reader and returns a tuple with an output provider for timed metadata groups buffers, and an associated random access controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputcaptionprovider(for:validationdelegate:))*