# init(assetReaderTrackOutput:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a caption adaptor that reads from a track output.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

## Declaration

```swift
init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)
```

```objc
- (instancetype) initWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *) trackOutput;
```

## Parameters

- `trackOutput`: The track output from which the system reads captions.

## See Also

### Creating a caption adaptor
- [+ assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:](./assetreaderoutputcaptionadaptorwithassetreadertrackoutput_.md)
  A class method that creates a caption adaptor that reads from a track output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/init(assetreadertrackoutput:))*