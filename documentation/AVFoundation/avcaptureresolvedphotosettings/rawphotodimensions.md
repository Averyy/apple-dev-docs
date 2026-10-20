# rawPhotoDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The size, in pixels, of the RAW-format photo image that the capture delivers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var rawPhotoDimensions: CMVideoDimensions { get }
```

```objc
@property (readonly) CMVideoDimensions rawPhotoDimensions;
```

#### Discussion

The output dimensions of a captured image are set at the moment of capture, depending on device orientation and capture session configuration. (For example, when the capture session includes a video output and video stabilization is in use, captured photos are smaller.)

This property provides the dimensions of the image to be delivered in the  [`photoOutput(_:didFinishProcessingPhoto:error:)`](../avcapturephotocapturedelegate/photooutput%28_,didfinishprocessingphoto,error%29.md) method. Use this property in earlier delegate methods to find the size of the image before delivery.

If you do not request capture in RAW format, this property’s value has zero width and zero height.

## See Also

### Examining output dimensions
- [var photoDimensions: CMVideoDimensions](./photodimensions.md)
  The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [var deferredPhotoProxyDimensions: CMVideoDimensions](./deferredphotoproxydimensions.md)
  The resolved dimensions of the photo proxy when using deferred photo delivery.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/rawphotodimensions)*