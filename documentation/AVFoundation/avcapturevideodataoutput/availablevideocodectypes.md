# availableVideoCodecTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableVideoCodecTypes;
```

#### Discussion

The value contains an array of video codecs that the output supports. Specify the codec it uses by setting a supported value for the [`AVVideoCodecKey`](../avvideocodeckey.md) entry in its [`videoSettings`](./videosettings.md) dictionary. The first format in the returned list is the most efficient output format.

## See Also

### Retrieving supported video types
- [var availableVideoPixelFormatTypes: [OSType]](./availablevideopixelformattypes.md)
  The video pixel formats the output supports.
- [func availableVideoCodecTypesForAssetWriter(writingTo: AVFileType) -> [AVVideoCodecType]](./availablevideocodectypesforassetwriter%28writingto%29.md)
  The video codecs that the output supports for writing video to the output file.
- [struct AVVideoCodecType](../avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.
- [availableVideoCVPixelFormatTypes](./availablevideocvpixelformattypes.md)
  The video pixel formats the output supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/availablevideocodectypes)*