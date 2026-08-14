# livePhotoMovieFileURL

**Framework**: AVFoundation  
**Kind**: property

A URL at which to write Live Photo movie output.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var livePhotoMovieFileURL: URL? { get set }
```

#### Discussion

Live Photos capture both a still image and a short movie, which the system presents together in user interfaces such as the Photos app. By default, this property’s value is `nil`, disabling Live Photo capture. Set this property to a file URL to capture Live Photos.

When you enable Live Photo capture, the following requirements apply:

- The photo output’s [`isLivePhotoCaptureEnabled`](avcapturephotooutput/islivephotocaptureenabled.md) property must be [`true`](https://developer.apple.com/documentation/swift/true), and its and [`isLivePhotoCaptureSuspended`](avcapturephotooutput/islivephotocapturesuspended.md) property must be [`false`](https://developer.apple.com/documentation/swift/false).
- The URL you specify must be a file URL to an accessible location in your app’s sandbox.
- Your delegate object must implement the [`photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md) method.

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## See Also

- [var livePhotoMovieMetadata: [AVMetadataItem]!](avcapturephotosettings/livephotomoviemetadata.md)
  A dictionary of metadata to include in the Live Photo movie file.
- [var livePhotoVideoCodecType: AVVideoCodecType](avcapturephotosettings/livephotovideocodectype.md)
  The video codec to use for encoding the movie portion of Live Photo output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotomoviefileurl)*