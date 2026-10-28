# dimensionsForSemanticSegmentationMatte(ofType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves the resolved dimensions of the semantic segmentation mattes that the photo output delivers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func dimensionsForSemanticSegmentationMatte(ofType semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType) -> CMVideoDimensions
```

```objc
- (CMVideoDimensions) dimensionsForSemanticSegmentationMatteOfType:(AVSemanticSegmentationMatteType) semanticSegmentationMatteType;
```

## Return Value

A [`CMVideoDimensions`](../../CoreMedia/cmvideodimensions.md) structure that provides the height and width of the image mattes.

## Parameters

- `semanticSegmentationMatteType`: The segmentation matte type for which to retrieve dimensions.

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
- [var photoProcessingTimeRange: CMTimeRange](./photoprocessingtimerange.md)
  The time range in which to expect the system to deliver the photo to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/dimensionsforsemanticsegmentationmatte(oftype:))*