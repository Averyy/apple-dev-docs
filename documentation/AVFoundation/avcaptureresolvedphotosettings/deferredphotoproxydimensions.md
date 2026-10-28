# deferredPhotoProxyDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The resolved dimensions of the photo proxy when using deferred photo delivery.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var deferredPhotoProxyDimensions: CMVideoDimensions { get }
```

```objc
@property (readonly) CMVideoDimensions deferredPhotoProxyDimensions;
```

## Discussion

When the system returns an [`AVCaptureDeferredPhotoProxy`](../avcapturedeferredphotoproxy.md), the [`photoDimensions`](./photodimensions.md) property of this object represents the dimensions of the final photo. If you don’t opt in to deferred photo delivery, this value has a width and height of 0.

## See Also

### Examining output dimensions
- [var photoDimensions: CMVideoDimensions](./photodimensions.md)
  The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [var rawPhotoDimensions: CMVideoDimensions](./rawphotodimensions.md)
  The size, in pixels, of the RAW-format photo image that the capture delivers.
- [var previewDimensions: CMVideoDimensions](./previewdimensions.md)
  The size, in pixels, of the preview image that the system delivers with the capture.
- [var embeddedThumbnailDimensions: CMVideoDimensions](./embeddedthumbnaildimensions.md)
  The size, in pixels, of the thumbnail image that the capture delivers.
- [var rawEmbeddedThumbnailDimensions: CMVideoDimensions](./rawembeddedthumbnaildimensions.md)
  The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [var livePhotoMovieDimensions: CMVideoDimensions](./livephotomoviedimensions.md)
  The size, in pixels, of the Live Photo movie content that the capture delivers.
- [var portraitEffectsMatteDimensions: CMVideoDimensions](./portraiteffectsmattedimensions.md)
  The size, in pixels, of the portrait effects matte that the capture delivers.
- [func dimensionsForSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions](./dimensionsforsemanticsegmentationmatte%28oftype%29.md)
  Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.
- [var photoProcessingTimeRange: CMTimeRange](./photoprocessingtimerange.md)
  The time range in which to expect the system to deliver the photo to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/deferredphotoproxydimensions)*