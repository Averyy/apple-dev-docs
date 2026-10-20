# photoProcessingTimeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time range in which to expect the system to deliver the photo to the delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var photoProcessingTimeRange: CMTimeRange { get }
```

```objc
@property (readonly) CMTimeRange photoProcessingTimeRange;
```

#### Discussion

Indicates the processing time range you can expect for this photo to be delivered to your delegate. the .start field of the CMTimeRange is zero-based. In other words, if photoProcessingTimeRange.start is equal to .5 seconds, then the minimum processing time for this photo is .5 seconds. The .start field plus the .duration field of the CMTimeRange indicate the max expected processing time for this photo. Consider implementing a UI affordance if the max processing time is uncomfortably long.

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
- [var livePhotoMovieDimensions: CMVideoDimensions](./livephotomoviedimensions.md)
  The size, in pixels, of the Live Photo movie content that the capture delivers.
- [var portraitEffectsMatteDimensions: CMVideoDimensions](./portraiteffectsmattedimensions.md)
  The size, in pixels, of the portrait effects matte that the capture delivers.
- [func dimensionsForSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions](./dimensionsforsemanticsegmentationmatte%28oftype%29.md)
  Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/photoprocessingtimerange)*