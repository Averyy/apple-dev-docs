# assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

A class method that creates a caption adaptor that reads from a track output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
+ (instancetype) assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *) trackOutput;
```

#### Return Value

A new instance of [`AVAssetReaderOutputCaptionAdaptor`](../avassetreaderoutputcaptionadaptor.md).

## Parameters

- `trackOutput`: The track output from which to read captions.

## See Also

### Creating a caption adaptor
- [init(assetReaderTrackOutput: AVAssetReaderTrackOutput)](./init%28assetreadertrackoutput%29.md)
  Creates a caption adaptor that reads from a track output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/assetreaderoutputcaptionadaptorwithassetreadertrackoutput:)*