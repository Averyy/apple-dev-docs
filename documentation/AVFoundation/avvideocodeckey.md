# AVVideoCodecKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key to access the name of the codec for compressing video.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVVideoCodecKey: String
```

```c
extern NSString * const AVVideoCodecKey;
```

## Mentions

- [Recording movies in alternative formats](./recording-movies-in-alternative-formats.md)

## Discussion

The value for this key is an instance of [`NSString`](../Foundation/nsstring.md), equivalent to [`CMVideoCodecType`](../CoreMedia/cmvideocodectype.md). Use this key to set the video compression format to H.264, HEVC, or JPEG, depending on the video codec types available in [`AVCaptureMovieFileOutput`](./avcapturemoviefileoutput.md). Check available video codec types by consulting [`availableVideoCodecTypes`](./avcapturemoviefileoutput/availablevideocodectypes.md).

## See Also

### Video codecs
- [struct AVVideoCodecType](./avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocodeckey)*