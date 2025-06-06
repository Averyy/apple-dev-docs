# embeddedThumbnailDimensions

**Framework**: Avfoundation  
**Kind**: property

The size, in pixels, of the thumbnail image that the capture delivers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var embeddedThumbnailDimensions: CMVideoDimensions { get }
```

#### Discussion

Use the [`embeddedThumbnailPhotoFormat`](avcapturephotosettings/embeddedthumbnailphotoformat.md) property in your photo settings object to request delivery of a thumbnail image alongside the main photo output from the capture. When you request a thumbnail, the photo output chooses dimensions that best match your requested size while preserving the aspect ratio of the captured photo. Aspect ratio is determined by capture format and by device orientation at the moment of capture.

> **Note**:  The photo capture system supports both  and  images as companions to the full-size primary image in a photo capture. A preview image is intended for immediate display (as seen when taking photos in the iOS Camera app), and as such is sized for full-screen presentation on the current device. A thumbnail image is intended for embedding in the output image file and can be used by other software (such as Quick Look in a file browser) to allow users to quickly review the image without loading the entire image file; the size of thumbnail images may be limited depending on the output file format.

This property provides the dimensions of the requested thumbnail image, which is delivered in the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method. Use this property in earlier delegate methods to find the size of the image before delivery.

If you do not request a thumbnail image, this property’s value has zero width and zero height.

## See Also

- [var photoDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/photodimensions.md)
  The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [var deferredPhotoProxyDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/deferredphotoproxydimensions.md)
  The resolved dimensions of the photo proxy when using deferred photo delivery.
- [var rawPhotoDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/rawphotodimensions.md)
  The size, in pixels, of the RAW-format photo image that the capture delivers.
- [var previewDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/previewdimensions.md)
  The size, in pixels, of the preview image that the system delivers with the capture.
- [var rawEmbeddedThumbnailDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/rawembeddedthumbnaildimensions.md)
  The size, in pixels, of the RAW-format embedded thumbnail image that the capture delivers.
- [var livePhotoMovieDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/livephotomoviedimensions.md)
  The size, in pixels, of the Live Photo movie content that the capture delivers.
- [var portraitEffectsMatteDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/portraiteffectsmattedimensions.md)
  The size, in pixels, of the portrait effects matte that the capture delivers.
- [func dimensionsForSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions](avcaptureresolvedphotosettings/dimensionsforsemanticsegmentationmatte(oftype:).md)
  Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.
- [var photoProcessingTimeRange: CMTimeRange](avcaptureresolvedphotosettings/photoprocessingtimerange.md)
  The time range in which to expect the system to deliver the photo to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/embeddedthumbnaildimensions)*