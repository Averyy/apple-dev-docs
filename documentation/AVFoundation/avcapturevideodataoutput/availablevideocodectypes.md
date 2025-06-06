# availableVideoCodecTypes

**Framework**: AVFoundation  
**Kind**: property

The video codecs that the output supports.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var availableVideoCodecTypes: [AVVideoCodecType] { get }
```

#### Discussion

The value contains an array of video codecs that the output supports. Specify the codec it uses by setting a supported value for the [`AVVideoCodecKey`](avvideocodeckey.md) entry in its [`videoSettings`](avcapturevideodataoutput/videosettings.md) dictionary. The first format in the returned list is the most efficient output format.

## See Also

- [var availableVideoPixelFormatTypes: [OSType]](avcapturevideodataoutput/availablevideopixelformattypes.md)
  The video pixel formats the output supports.
- [func availableVideoCodecTypesForAssetWriter(writingTo: AVFileType) -> [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:).md)
  The video codecs that the output supports for writing video to the output file.
- [struct AVVideoCodecType](avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypes)*