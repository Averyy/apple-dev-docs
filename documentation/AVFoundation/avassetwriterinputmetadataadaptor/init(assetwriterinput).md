# init(assetWriterInput:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a metadata group adaptor to append timed metadata groups to write to an output file.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputMetadataReceiver(for:) instead

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput)
```

```objc
- (instancetype) initWithAssetWriterInput:(AVAssetWriterInput *) input;
```

## Parameters

- `input`: The metadata input to which to append groups of timed metadata.

## See Also

### Creating an input metadata adaptor
- [+ assetWriterInputMetadataAdaptorWithAssetWriterInput:](./assetwriterinputmetadataadaptorwithassetwriterinput_.md)
  Returns a new metadata adaptor to append timed metadata groups to write to an output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/init(assetwriterinput:))*