# AVCaptureResolvedPhotoSettings

**Framework**: AVFoundation  
**Kind**: class

A description of the features and settings in use for an in-progress or complete photo capture request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureResolvedPhotoSettings
```

## Mentions

- [Configuring Camera Capture to Collect a Portrait Effects Matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)

#### Overview

When you request a photo capture using the [`AVCapturePhotoOutput`](avcapturephotooutput.md) [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, you describe the settings for that capture request in an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object. When the capture begins, the photo output calls your delegate methods and provides an [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object detailing the settings that are in effect for that capture. Resolved photo settings objects are immutable; they describe a request that has already been made.

The [`uniqueID`](avcaptureresolvedphotosettings/uniqueid.md) property of a resolved photo settings object passed to one of your [`AVCapturePhotoCaptureDelegate`](avcapturephotocapturedelegate.md) methods matches the [`uniqueID`](avcapturephotosettings/uniqueid.md) value of the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you passed when requesting capture. Use this value to determine which delegate method calls correspond to which capture requests.

Some photo capture settings are automatic, such as the [`flashMode`](avcapturephotosettings/flashmode.md) property. For such settings, the photo output determines whether to use that feature at the moment of capture—you don’t know when requesting a capture whether the feature is active when the capture completes. When the photo output calls your delegate methods, the provided [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object details which automatic features have been set for that capture.

Likewise, the dimensions of an output image or movie may not be set until the moment of capture. For example, when you specify a thumbnail size with the [`previewPhotoFormat`](avcapturephotosettings/previewphotoformat.md) setting, the photo output chooses dimensions that best match your requested size while preserving the aspect ratio of the captured photo. When the photo output calls your delegate methods, use the [`previewDimensions`](avcaptureresolvedphotosettings/previewdimensions.md) property of the resolved settings to find the actual preview image dimensions. See the methods listed in Examining Output Dimensions for other cases where output dimensions can change at capture time.

## Topics

### Resolving Photo Capture Requests
- [var uniqueID: Int64](avcaptureresolvedphotosettings/uniqueid.md)
  The unique identifier for the photo capture this settings object corresponds to.
- [var expectedPhotoCount: Int](avcaptureresolvedphotosettings/expectedphotocount.md)
  The number of photo capture results in the capture request.
### Examining Photo Capture Settings
- [var isFlashEnabled: Bool](avcaptureresolvedphotosettings/isflashenabled.md)
  A Boolean value indicating whether the camera flash fires for this capture.
- [var isRedEyeReductionEnabled: Bool](avcaptureresolvedphotosettings/isredeyereductionenabled.md)
  A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.
- [var isVirtualDeviceFusionEnabled: Bool](avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md)
  A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [var isFastCapturePrioritizationEnabled: Bool](avcaptureresolvedphotosettings/isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [var isContentAwareDistortionCorrectionEnabled: Bool](avcaptureresolvedphotosettings/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [var isStillImageStabilizationEnabled: Bool](avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md)
  A Boolean value indicating whether this capture uses image stabilization.
- [var isDualCameraFusionEnabled: Bool](avcaptureresolvedphotosettings/isdualcamerafusionenabled.md)
  A Boolean value indicating whether this capture combines image data from a dual camera.
### Examining Output Dimensions
- [var photoDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/photodimensions.md)
  The size, in pixels, of the photo image (in a processed format, such as JPEG) that the capture delivers.
- [var deferredPhotoProxyDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/deferredphotoproxydimensions.md)
  The resolved dimensions of the photo proxy when using deferred photo delivery.
- [var rawPhotoDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/rawphotodimensions.md)
  The size, in pixels, of the RAW-format photo image that the capture delivers.
- [var previewDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/previewdimensions.md)
  The size, in pixels, of the preview image that the system delivers with the capture.
- [var embeddedThumbnailDimensions: CMVideoDimensions](avcaptureresolvedphotosettings/embeddedthumbnaildimensions.md)
  The size, in pixels, of the thumbnail image that the capture delivers.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCapturePhotoSettings](avcapturephotosettings.md)
  A specification of the features and settings to use for a single photo capture request.
- [class AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md)
  A specification of the features and settings to use for a photo capture request that captures multiple images with varied settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings)*