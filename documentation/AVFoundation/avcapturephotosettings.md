# AVCapturePhotoSettings

**Framework**: AVFoundation  
**Kind**: class

A specification of the features and settings to use for a single photo capture request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class AVCapturePhotoSettings
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)
- [Capturing and Saving Live Photos](capturing-and-saving-live-photos.md)
- [Saving Captured Photos](saving-captured-photos.md)
- [Capturing Photos with Depth](capturing-photos-with-depth.md)
- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)

#### Overview

To take a photo, you create and configure a [`AVCapturePhotoSettings`](avcapturephotosettings.md) object, then pass it to the [`AVCapturePhotoOutput`](avcapturephotooutput.md) [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method.

A [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance can include any combination of settings, regardless of whether that combination is valid for a given capture session. When you initiate a capture by passing a photo settings object to the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, the photo capture output validates your settings to ensure deterministic behavior. For example, the [`flashMode`](avcapturephotosettings/flashmode.md) setting must specify a value that’s present in the photo output’s [`supportedFlashModes`](avcapturephotooutput/supportedflashmodes-4u69s.md) array. For detailed validation rules, see each property description below.

> ❗ **Important**:  You can’t reuse a [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance for multiple captures. Calling the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception)) if the `settings` object’s [`uniqueID`](avcapturephotosettings/uniqueid.md) value matches that of any previously used settings object. To reuse a specific combination of settings, use the [`init(from:)`](avcapturephotosettings/init(from:).md) initializer to create a new, unique [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance from an existing photo settings object.

 You can’t reuse a [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance for multiple captures. Calling the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception)) if the `settings` object’s [`uniqueID`](avcapturephotosettings/uniqueid.md) value matches that of any previously used settings object.

To reuse a specific combination of settings, use the [`init(from:)`](avcapturephotosettings/init(from:).md) initializer to create a new, unique [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance from an existing photo settings object.

## Topics

### Creating photo settings
- [convenience init(format: [String : Any]?)](avcapturephotosettings/init(format:).md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType)](avcapturephotosettings/init(rawpixelformattype:).md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](avcapturephotosettings/init(rawpixelformattype:processedformat:).md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:).md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [convenience init(from: AVCapturePhotoSettings)](avcapturephotosettings/init(from:).md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.
### Inspecting settings
- [var uniqueID: Int64](avcapturephotosettings/uniqueid.md)
  A unique identifier for this photo settings instance.
- [var format: [String : Any]?](avcapturephotosettings/format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var processedFileType: AVFileType?](avcapturephotosettings/processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawFileType: AVFileType?](avcapturephotosettings/rawfiletype.md)
  The container file format for eventual output of the RAW image.
- [var rawPhotoPixelFormatType: OSType](avcapturephotosettings/rawphotopixelformattype.md)
  An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.
### Configuring photo settings
- [var flashMode: AVCaptureDevice.FlashMode](avcapturephotosettings/flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](avcapturephotosettings/isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [var maxPhotoDimensions: CMVideoDimensions](avcapturephotosettings/maxphotodimensions.md)
  The maximum resolution of the photo to capture.
- [var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](avcapturephotosettings/photoqualityprioritization.md)
  A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [var isCameraCalibrationDataDeliveryEnabled: Bool](avcapturephotosettings/iscameracalibrationdatadeliveryenabled.md)
  A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [var isAutoContentAwareDistortionCorrectionEnabled: Bool](avcapturephotosettings/isautocontentawaredistortioncorrectionenabled.md)
  A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [var isAutoVirtualDeviceFusionEnabled: Bool](avcapturephotosettings/isautovirtualdevicefusionenabled.md)
  A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [var virtualDeviceConstituentPhotoDeliveryEnabledDevices: [AVCaptureDevice]](avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices.md)
  The constituent devices for which the virtual device should deliver photos.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that determines whether a dual camera device delivers images from both cameras.
- [var isAutoDualCameraFusionEnabled: Bool](avcapturephotosettings/isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.
### Suppressing the Shutter Sound
- [var isShutterSoundSuppressionEnabled: Bool](avcapturephotosettings/isshuttersoundsuppressionenabled.md)
  A Boolean value that indicates whether to suppress the built-in shutter sound when capturing a photo.
### Enabling Preview and Thumbnail Delivery
- [var previewPhotoFormat: [String : Any]?](avcapturephotosettings/previewphotoformat.md)
  A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [var availablePreviewPhotoPixelFormatTypes: [OSType]](avcapturephotosettings/availablepreviewphotopixelformattypes-30d9.md)
  An array of available of pixel format types available to specify a preview photo format.
- [var embeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/embeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [var rawEmbeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/rawembeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availableembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
### Configuring Live Photo Settings
- [var livePhotoMovieFileURL: URL?](avcapturephotosettings/livephotomoviefileurl.md)
  A URL at which to write Live Photo movie output.
- [var livePhotoMovieMetadata: [AVMetadataItem]!](avcapturephotosettings/livephotomoviemetadata.md)
  A dictionary of metadata to include in the Live Photo movie file.
- [var livePhotoVideoCodecType: AVVideoCodecType](avcapturephotosettings/livephotovideocodectype.md)
  The video codec to use for encoding the movie portion of Live Photo output.
### Configuring Constant Color
- [var isConstantColorEnabled: Bool](avcapturephotosettings/isconstantcolorenabled.md)
  A Boolean value that indicates whether to capture the photo with constant color.
- [var isConstantColorFallbackPhotoDeliveryEnabled: Bool](avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled.md)
  A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.
### Capturing Depth Data
- [var isDepthDataDeliveryEnabled: Bool](avcapturephotosettings/isdepthdatadeliveryenabled.md)
  A Boolean value that determines whether the photo output captures depth data along with the photo.
- [var embedsDepthDataInPhoto: Bool](avcapturephotosettings/embedsdepthdatainphoto.md)
  A Boolean value that determines whether any depth data captured with the photo is included when generating output file data.
- [var isDepthDataFiltered: Bool](avcapturephotosettings/isdepthdatafiltered.md)
  A Boolean value that determines whether to smooth noise and fill in missing values in depth data output.
### Capturing Portrait Effects Matte
- [var isPortraitEffectsMatteDeliveryEnabled: Bool](avcapturephotosettings/isportraiteffectsmattedeliveryenabled.md)
  Specifies whether a portrait effects matte should be captured along with the photo.
- [var embedsPortraitEffectsMatteInPhoto: Bool](avcapturephotosettings/embedsportraiteffectsmatteinphoto.md)
  Specifies whether the portrait effects matte captured with ths photo should be written to the photo’s file structure.
### Capturing Semantic Segmentation Mattes
- [var embedsSemanticSegmentationMattesInPhoto: Bool](avcapturephotosettings/embedssemanticsegmentationmattesinphoto.md)
  A Boolean value that specifies whether to write the enabled semantic segmentation matte types captured with this photo to the photo’s file structure.
- [var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](avcapturephotosettings/enabledsemanticsegmentationmattetypes.md)
  An array of semantic segmentation matte types that the photo render pipeline can deliver.
### Embedding Metadata
- [var metadata: [String : Any]](avcapturephotosettings/metadata.md)
  A dictionary of metadata keys and values to embed in photo file output.
### Instance Properties
- [var rawFileFormat: [String : Any]?](avcapturephotosettings/rawfileformat.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md)
  A specification of the features and settings to use for a photo capture request that captures multiple images with varied settings.
- [class AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md)
  A description of the features and settings in use for an in-progress or complete photo capture request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings)*