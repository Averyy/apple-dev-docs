# availableVideoCVPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video pixel formats the output supports.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * availableVideoCVPixelFormatTypes;
```

#### Discussion

This value contains an array of video formats, in unspecified order, that the output supports. You can set the format by specifying it as the [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md) entry in the output’s [`videoSettings`](./videosettings.md) dictionary.

> **Note**:  The contents of this list may change if the video capture device’s [`activeFormat`](../avcapturedevice/activeformat.md) value changes.

## See Also

### Retrieving supported video types
- [var availableVideoCodecTypes: [AVVideoCodecType]](./availablevideocodectypes.md)
  The video codecs that the output supports.
- [func availableVideoCodecTypesForAssetWriter(writingTo: AVFileType) -> [AVVideoCodecType]](./availablevideocodectypesforassetwriter%28writingto%29.md)
  The video codecs that the output supports for writing video to the output file.
- [struct AVVideoCodecType](../avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocvpixelformattypes)*