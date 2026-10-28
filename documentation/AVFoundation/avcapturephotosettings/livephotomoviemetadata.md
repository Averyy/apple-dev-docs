# livePhotoMovieMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A dictionary of metadata to include in the Live Photo movie file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var livePhotoMovieMetadata: [AVMetadataItem]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<AVMetadataItem *> * livePhotoMovieMetadata;
```

## Discussion

Live Photos capture both a still image and a short movie, which the system presents together in user interfaces such as the Photos app. A Live Photo movie always contains a `AVMetadataQuickTimeMetadataKeyContentIdentifier` key, associating the movie with a similar identifier in the [`kCGImagePropertyExifMakerNote`](../../ImageIO/kcgimagepropertyexifmakernote.md) property of the corresponding still image. The photo capture output automatically generates a unique content identifier for you if you don’t specify one of your own. You can also use this property to specify additional movie metadata.

This property applies only if the value of the [`livePhotoMovieFileURL`](./livephotomoviefileurl.md) property is to non-`nil`.

## See Also

### Configuring Live Photo settings
- [var livePhotoMovieFileURL: URL?](./livephotomoviefileurl.md)
  A URL at which to write Live Photo movie output.
- [var livePhotoVideoCodecType: AVVideoCodecType](./livephotovideocodectype.md)
  The video codec to use for encoding the movie portion of Live Photo output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotomoviemetadata)*