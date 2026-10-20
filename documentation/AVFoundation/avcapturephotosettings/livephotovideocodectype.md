# livePhotoVideoCodecType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video codec to use for encoding the movie portion of Live Photo output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var livePhotoVideoCodecType: AVVideoCodecType { get set }
```

```objc
@property (nonatomic, copy) AVVideoCodecType livePhotoVideoCodecType;
```

#### Discussion

This value must be one of the video codec types listed in the photo output’s [`availableLivePhotoVideoCodecTypes`](../avcapturephotooutput/availablelivephotovideocodectypes.md) array.

## See Also

### Configuring Live Photo settings
- [var livePhotoMovieFileURL: URL?](./livephotomoviefileurl.md)
  A URL at which to write Live Photo movie output.
- [var livePhotoMovieMetadata: [AVMetadataItem]!](./livephotomoviemetadata.md)
  A dictionary of metadata to include in the Live Photo movie file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotovideocodectype)*