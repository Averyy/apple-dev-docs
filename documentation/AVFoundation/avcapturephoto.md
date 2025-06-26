# AVCapturePhoto

**Framework**: AVFoundation  
**Kind**: class

A container for image data from a photo capture output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class AVCapturePhoto
```

## Mentions

- [Configuring Camera Capture to Collect a Portrait Effects Matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
- [Saving Captured Photos](saving-captured-photos.md)
- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)
- [Capturing and Saving Live Photos](capturing-and-saving-live-photos.md)
- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)
- [Capturing Uncompressed Image Data](capturing-uncompressed-image-data.md)
- [Capturing Photos with Depth](capturing-photos-with-depth.md)
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Overview

When you capture photos with the [`AVCapturePhotoOutput`](avcapturephotooutput.md) class, your delegate object receives each resulting image and related data in the form of an [`AVCapturePhoto`](avcapturephoto.md) object. This object is an immutable wrapper from which you can retrieve various results of the photo capture.

In addition to the photo image pixel buffer, an AVCapturePhoto object can also contain a preview-sized pixel buffer, capture metadata, and, on supported devices, depth data and camera calibration data. From an [`AVCapturePhoto`](avcapturephoto.md) object, you can generate data appropriate for writing to a file, such as HEVC encoded image data containerized in the HEIC file format and including a preview image, depth data and other attachments.

An [`AVCapturePhoto`](avcapturephoto.md) instance wraps a single image result. For example, if you request a bracketed capture of three images, your callback is called three times, each time delivering a single [`AVCapturePhoto`](avcapturephoto.md) object.

## Topics

### Resolving Photo Capture Requests
- [var resolvedSettings: AVCaptureResolvedPhotoSettings](avcapturephoto/resolvedsettings.md)
  The settings object that was used to request this photo capture.
- [var photoCount: Int](avcapturephoto/photocount.md)
  The 1-based index of this photo capture relative to other results from the same capture request.
- [var timestamp: CMTime](avcapturephoto/timestamp.md)
  The time at which the image was captured.
### Accessing Photo Pixel Data
- [var isRawPhoto: Bool](avcapturephoto/israwphoto.md)
  A Boolean value indicating whether this photo object contains RAW format data.
- [var pixelBuffer: CVPixelBuffer?](avcapturephoto/pixelbuffer.md)
  The uncompressed or RAW image sample buffer for the photo, if requested.
### Accessing Preview Photo Data
- [var embeddedThumbnailPhotoFormat: [String : Any]?](avcapturephoto/embeddedthumbnailphotoformat.md)
  A dictionary describing the data format for a preview-sized image accompanying the captured photo.
- [var previewPixelBuffer: CVPixelBuffer?](avcapturephoto/previewpixelbuffer.md)
  The pixel data for a preview-sized version of the photo, if requested.
### Accessing Photo Metadata
- [var depthData: AVDepthData?](avcapturephoto/depthdata.md)
  Depth or disparity map data captured with the photo.
- [var cameraCalibrationData: AVCameraCalibrationData?](avcapturephoto/cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcapturephoto/sourcedevicetype.md)
  The type of device that captured the photo.
- [var metadata: [String : Any]](avcapturephoto/metadata.md)
  A dictionary of metadata describing the captured image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](avcapturephoto/portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.
### Packaging Data for File Output
- [func fileDataRepresentation(with: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?](avcapturephoto/filedatarepresentation(with:).md)
  Gets a customized representation of the photo data.
- [protocol AVCapturePhotoFileDataRepresentationCustomizer](avcapturephotofiledatarepresentationcustomizer.md)
  A protocol that defines the methods to implement to customize the packaging of photo data.
- [func fileDataRepresentation() -> Data?](avcapturephoto/filedatarepresentation.md)
  Generates and returns a flat data representation of the photo and its attachments.
- [func cgImageRepresentation() -> CGImage?](avcapturephoto/cgimagerepresentation.md)
  Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [func previewCGImageRepresentation() -> CGImage?](avcapturephoto/previewcgimagerepresentation.md)
  Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [func fileDataRepresentation(withReplacementMetadata: [String : Any]?, replacementEmbeddedThumbnailPhotoFormat: [String : Any]?, replacementEmbeddedThumbnailPixelBuffer: CVPixelBuffer?, replacementDepthData: AVDepthData?) -> Data?](avcapturephoto/filedatarepresentation(withreplacementmetadata:replacementembeddedthumbnailphotoformat:replacementembeddedthumbnailpixelbuffer:replacementdepthdata:).md)
  Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments.
### Enabling Constant Color
- [var constantColorCenterWeightedMeanConfidenceLevel: Float](avcapturephoto/constantcolorcenterweightedmeanconfidencelevel.md)
  A score that summarizes the overall confidence level of a constant color photo.
- [var constantColorConfidenceMap: CVPixelBuffer?](avcapturephoto/constantcolorconfidencemap.md)
  A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.
- [var isConstantColorFallbackPhoto: Bool](avcapturephoto/isconstantcolorfallbackphoto.md)
  A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.
### Examining Bracketed Capture Information
- [var bracketSettings: AVCaptureBracketedStillImageSettings?](avcapturephoto/bracketsettings.md)
  The variations available for bracketed capture settings for this photo.
- [var sequenceCount: Int](avcapturephoto/sequencecount.md)
  The 1-based index of this photo in a bracketed capture sequence.
- [var lensStabilizationStatus: AVCaptureDevice.LensStabilizationStatus](avcapturephoto/lensstabilizationstatus.md)
  Information about the use of lens stabilization during bracketed photo capture.
- [AVCaptureDevice.LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md)
  Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.
### Accessing Segmentation Mattes
- [func semanticSegmentationMatte(for: AVSemanticSegmentationMatte.MatteType) -> AVSemanticSegmentationMatte?](avcapturephoto/semanticsegmentationmatte(for:).md)
  Retrieves the semantic segmentation matte associated with this photo.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Capturing consistent color images](capturing-consistent-color-images.md)
  Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing Still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [class AVCapturePhotoOutput](avcapturephotooutput.md)
  A capture output for still image, Live Photos, and other photography workflows.
- [protocol AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md)
  Methods for monitoring progress and receiving results from a photo capture output.
- [class AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md)
  An object that monitors changes to a photo output’s capture readiness.
- [protocol AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md)
  A delegate protocol to receive updates about a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto)*