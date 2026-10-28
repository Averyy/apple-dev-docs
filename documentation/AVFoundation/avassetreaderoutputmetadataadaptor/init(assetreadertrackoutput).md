# init(assetReaderTrackOutput:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an object that reads timed metadata groups from an asset reader output.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputMetadataProvider(for:) instead

## Declaration

```swift
init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)
```

```objc
- (instancetype) initWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *) trackOutput;
```

## Discussion

You can only create an adaptor with a track output that vends metadata, and that isn’t associated with another adaptor instance. Likewise, you can only create an adaptor with a track output whose asset reader hasn’t started reading.

> ❗ **Important**:  Don’t call the [`copyNextSampleBuffer()`](../avassetreaderoutput/copynextsamplebuffer%28%29.md) method on the track output after you use it to initialize a timed metadata adaptor. Calling the track output’s [`copyNextSampleBuffer()`](../avassetreaderoutput/copynextsamplebuffer%28%29.md) method after this occurs results in the system throwing an exception.

## Parameters

- `trackOutput`: A track output that vends sample buffers that contain metadata.

## See Also

### Creating a metadata adaptor
- [+ assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:](./assetreaderoutputmetadataadaptorwithassetreadertrackoutput_.md)
  Returns a new object that reads timed metadata groups from an asset reader output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/init(assetreadertrackoutput:))*