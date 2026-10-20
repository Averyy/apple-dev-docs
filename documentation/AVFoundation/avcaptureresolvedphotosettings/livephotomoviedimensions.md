# livePhotoMovieDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The size, in pixels, of the Live Photo movie content that the capture delivers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var livePhotoMovieDimensions: CMVideoDimensions { get }
```

```objc
@property (readonly) CMVideoDimensions livePhotoMovieDimensions;
```

#### Discussion

Use the [`livePhotoMovieFileURL`](../avcapturephotosettings/livephotomoviefileurl.md) property in your photo settings object to request Live Photo capture. Live Photo movie dimensions can change depending on which device camera is used for capture.

This property provides dimensions for the movie content of the Live Photo, which is delivered in the [`photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)`](../avcapturephotocapturedelegate/photooutput%28_,didfinishprocessinglivephototomoviefileat,duration,photodisplaytime,resolvedsettings,error%29.md) method. Use this property in earlier delegate methods to find the dimensions of the movie before delivery.

For the dimensions of the static photo content of a Live Photo, see the [`photoDimensions`](./photodimensions.md) property.

If you do not request Live Photo capture, this property’s value has zero width and zero height.

## See Also

### Examining output dimensions
- [var photoDimensions: CMVideoDimensions](./photodimensions.md)
  The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [var deferredPhotoProxyDimensions: CMVideoDimensions](./deferredphotoproxydimensions.md)
  The resolved dimensions of the photo proxy when using deferred photo delivery.
- [var rawPhotoDimensions: CMVideoDimensions](./rawphotodimensions.md)
  The size, in pixels, of the RAW-format photo image that the capture delivers.
- [var previewDimensions: CMVideoDimensions](./previewdimensions.md)
  The size, in pixels, of the preview image that the system delivers with the capture.
- [var embeddedThumbnailDimensions: CMVideoDimensions](./embeddedthumbnaildimensions.md)
  The size, in pixels, of the thumbnail image that the capture delivers.
- [var rawEmbeddedThumbnailDimensions: CMVideoDimensions](./rawembeddedthumbnaildimensions.md)
  The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [var portraitEffectsMatteDimensions: CMVideoDimensions](./portraiteffectsmattedimensions.md)
  The size, in pixels, of the portrait effects matte that the capture delivers.
- [func dimensionsForSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions](./dimensionsforsemanticsegmentationmatte%28oftype%29.md)
  Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.
- [var photoProcessingTimeRange: CMTimeRange](./photoprocessingtimerange.md)
  The time range in which to expect the system to deliver the photo to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/livephotomoviedimensions)*