# availableVideoPixelFormatTypes

**Framework**: Avfoundation  
**Kind**: property

The video pixel formats the output supports.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var availableVideoPixelFormatTypes: [OSType] { get }
```

#### Discussion

This value contains an array of video formats, in unspecified order, that the output supports. You can set the format by specifying it as the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) entry in the output’s [`videoSettings`](avcapturevideodataoutput/videosettings.md) dictionary.

> **Note**:  The contents of this list may change if the video capture device’s [`activeFormat`](avcapturedevice/activeformat.md) value changes.

## See Also

- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypes.md)
  The video codecs that the output supports.
- [func availableVideoCodecTypesForAssetWriter(writingTo: AVFileType) -> [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:).md)
  The video codecs that the output supports for writing video to the output file.
- [struct AVVideoCodecType](avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideopixelformattypes)*