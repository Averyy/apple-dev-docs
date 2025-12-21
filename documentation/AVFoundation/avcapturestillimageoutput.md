# AVCaptureStillImageOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output for capturing still photos.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class AVCaptureStillImageOutput
```

## Topics

### Capturing an image
- [func captureStillImageAsynchronously(from: AVCaptureConnection, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:).md)
  Initiates a still image capture and returns immediately.
- [var isCapturingStillImage: Bool](avcapturestillimageoutput/iscapturingstillimage.md)
  Indicates whether a still image is being captured.
### Getting and setting image stabilization settings
- [var isStillImageStabilizationActive: Bool](avcapturestillimageoutput/isstillimagestabilizationactive.md)
  Indicates whether still image stabilization is in use for the current capture.
- [var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool](avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.md)
  A Boolean value that indicates whether still image stabilization should be automatically enabled.
- [var isStillImageStabilizationSupported: Bool](avcapturestillimageoutput/isstillimagestabilizationsupported.md)
  A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.
### Configuring orientation compensation
- [var isCameraSensorOrientationCompensationSupported: Bool](avcapturestillimageoutput/iscamerasensororientationcompensationsupported.md)
- [var isCameraSensorOrientationCompensationEnabled: Bool](avcapturestillimageoutput/iscamerasensororientationcompensationenabled.md)
### Configuring image settings
- [var isHighResolutionStillImageOutputEnabled: Bool](avcapturestillimageoutput/ishighresolutionstillimageoutputenabled.md)
  A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.
- [var availableImageDataCVPixelFormatTypes: [NSNumber]](avcapturestillimageoutput/availableimagedatacvpixelformattypes.md)
  The supported image pixel formats that can be specified as output settings.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](avcapturestillimageoutput/availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [var outputSettings: [String : Any]](avcapturestillimageoutput/outputsettings.md)
  The compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
### Image format conversion
- [class func jpegStillImageNSDataRepresentation(CMSampleBuffer) -> Data?](avcapturestillimageoutput/jpegstillimagensdatarepresentation(_:).md)
  Returns an `NSData` representation of a still image data and metadata attachments in a JPEG sample buffer.
### Still image bracketed capture
- [func captureStillImageBracketAsynchronously(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)](avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:).md)
  Captures a still image bracket.
- [var maxBracketedCaptureStillImageCount: Int](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md)
  Specifies the maximum number of still images that may be taken in a single bracket.
- [func prepareToCaptureStillImageBracket(from: AVCaptureConnection, withSettingsArray: [AVCaptureBracketedStillImageSettings], completionHandler: (Bool, (any Error)?) -> Void)](avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:).md)
  Allows the receiver to prepare resources in advance of capturing a still image bracket.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.
- [var isLensStabilizationDuringBracketedCaptureEnabled: Bool](avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.md)
  A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.
### Creating still image output
- [init()](avcapturestillimageoutput/init.md)
  Creates new still image output.

## Relationships

### Inherits From
- [AVCaptureOutput](avcaptureoutput.md)
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
- [Capturing still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](avcapturephoto.md)
  A container for image data from a photo capture output.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput)*