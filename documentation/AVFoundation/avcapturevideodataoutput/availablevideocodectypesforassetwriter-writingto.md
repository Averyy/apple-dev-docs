# availableVideoCodecTypesForAssetWriter(writingTo:)

**Framework**: AVFoundation  
**Kind**: method

The video codecs that the output supports for writing video to the output file.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func availableVideoCodecTypesForAssetWriter(writingTo outputFileType: AVFileType) -> [AVVideoCodecType]
```

#### Return Value

An array of video codecs.

## Parameters

- `outputFileType`: The UTI of the output file type.

## See Also

- [var availableVideoPixelFormatTypes: [OSType]](avcapturevideodataoutput/availablevideopixelformattypes.md)
  The video pixel formats the output supports.
- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypes.md)
  The video codecs that the output supports.
- [struct AVVideoCodecType](avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:))*