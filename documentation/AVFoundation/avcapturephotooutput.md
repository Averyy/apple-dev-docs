# AVCapturePhotoOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output for still image, Live Photos, and other photography workflows.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
class AVCapturePhotoOutput
```

## Mentions

- [Configuring Camera Capture to Collect a Portrait Effects Matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
- [Setting Up a Capture Session](setting-up-a-capture-session.md)
- [Capturing and Saving Live Photos](capturing-and-saving-live-photos.md)
- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)
- [Saving Captured Photos](saving-captured-photos.md)
- [Capturing Photos with Depth](capturing-photos-with-depth.md)
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)
- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)

#### Overview

[`AVCapturePhotoOutput`](avcapturephotooutput.md) provides an interface for capture workflows related to still photography. In addition to basic capture of still images, a photo output supports RAW-format capture, bracketed capture of multiple images, Live Photos, and wide-gamut color. You can output captured photos in a variety of formats and codecs, including RAW format DNG files, HEVC format HEIF files, and JPEG files.

To capture photos with the [`AVCapturePhotoOutput`](avcapturephotooutput.md) class, follow these steps:

1. Create an [`AVCapturePhotoOutput`](avcapturephotooutput.md) object. Use its properties to determine supported capture settings and to enable certain features (for example, whether to capture Live Photos).
2. Create and configure an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object to choose features and settings for a specific capture (for example, whether to enable image stabilization or flash).
3. Capture an image by passing your photo settings object to the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method along with a delegate object implementing the [`AVCapturePhotoCaptureDelegate`](avcapturephotocapturedelegate.md) protocol. The photo capture output then calls your delegate to notify you of significant events during the capture process.

Some photo capture settings, such as the [`flashMode`](avcapturephotosettings/flashmode.md) property, include options for automatic behavior. For such settings, the photo output determines whether to use that feature at the moment of capture—you don’t know when requesting a capture whether the feature will be enabled when the capture completes. When the photo capture output calls your [`AVCapturePhotoCaptureDelegate`](avcapturephotocapturedelegate.md) methods with information about the completed or in-progress capture, it also provides an [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object that details which automatic features are set for that capture. The resolved settings object’s [`uniqueID`](avcaptureresolvedphotosettings/uniqueid.md) property matches the [`uniqueID`](avcapturephotosettings/uniqueid.md) value of the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you used to request capture.

Enabling certain photo features (Live Photo capture and high resolution capture) requires a reconfiguration of the capture render pipeline. To opt into these features, set the [`isHighResolutionCaptureEnabled`](avcapturephotooutput/ishighresolutioncaptureenabled.md), [`isLivePhotoCaptureEnabled`](avcapturephotooutput/islivephotocaptureenabled.md), and [`isLivePhotoAutoTrimmingEnabled`](avcapturephotooutput/islivephotoautotrimmingenabled.md) properties before calling your [`AVCaptureSession`](avcapturesession.md) object’s [`startRunning()`](avcapturesession/startrunning().md) method. Changing any of these properties while the session is running disrupts the capture render pipeline: Live Photo captures in progress end immediately, unfulfilled photo requests abort, and video preview temporarily freezes.

Using a photo capture output adds other requirements to your [`AVCaptureSession`](avcapturesession.md) object:

- A capture session can’t support both Live Photo capture and movie file output. If your capture session includes an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) object, the [`isLivePhotoCaptureSupported`](avcapturephotooutput/islivephotocapturesupported.md) property becomes [`false`](https://developer.apple.com/documentation/swift/false). (As an alternative, you can use the [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) class to output video buffers at the same resolution as a simultaneous Live Photo capture).
- A capture session can’t contain both an [`AVCapturePhotoOutput`](avcapturephotooutput.md) object and an [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) object. The [`AVCapturePhotoOutput`](avcapturephotooutput.md) class includes all functionality of (and deprecates) the [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) class.

The [`AVCapturePhotoOutput`](avcapturephotooutput.md) class implicitly supports wide-gamut color photography. If the source [`AVCaptureDevice`](avcapturedevice.md) object’s [`activeColorSpace`](avcapturedevice/activecolorspace.md) value is [`AVCaptureColorSpace.P3_D65`](avcapturecolorspace/p3_d65.md), the capture output produces photos with wide color information (unless your [`AVCapturePhotoSettings`](avcapturephotosettings.md) object specifies an output format that doesn’t support wide color).

## Topics

### Creating a Photo Output
- [init()](avcapturephotooutput/init.md)
  Creates a new photo capture output object.
### Capturing a Photo
- [func capturePhoto(with: AVCapturePhotoSettings, delegate: any AVCapturePhotoCaptureDelegate)](avcapturephotooutput/capturephoto(with:delegate:).md)
  Initiates a photo capture using the specified settings.
### Managing Responsive Capture
- [var captureReadiness: AVCapturePhotoOutput.CaptureReadiness](avcapturephotooutput/capturereadiness-swift.property.md)
  A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [AVCapturePhotoOutput.CaptureReadiness](avcapturephotooutput/capturereadiness-swift.enum.md)
  Constants that indicate whether the output is ready to receive capture requests.
- [var isAutoDeferredPhotoDeliveryEnabled: Bool](avcapturephotooutput/isautodeferredphotodeliveryenabled.md)
  A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [var isAutoDeferredPhotoDeliverySupported: Bool](avcapturephotooutput/isautodeferredphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [var isFastCapturePrioritizationSupported: Bool](avcapturephotooutput/isfastcaptureprioritizationsupported.md)
  A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [var isFastCapturePrioritizationEnabled: Bool](avcapturephotooutput/isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the output enables fast capture prioritization.
- [var isResponsiveCaptureSupported: Bool](avcapturephotooutput/isresponsivecapturesupported.md)
  A Boolean value that indicates whether the photo output supports responsive capture.
- [var isResponsiveCaptureEnabled: Bool](avcapturephotooutput/isresponsivecaptureenabled.md)
  A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [var isZeroShutterLagSupported: Bool](avcapturephotooutput/iszeroshutterlagsupported.md)
  A Boolean value that indicates whether the photo output supports zero shutter lag.
- [var isZeroShutterLagEnabled: Bool](avcapturephotooutput/iszeroshutterlagenabled.md)
  A Boolean value that indicates whether the photo output configuration enables zero shutter lag.
### Determining Supported Pixel Formats
- [var availablePhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablephotopixelformattypes-3ydgm.md)
  The pixel formats the capture output supports for photo capture.
- [var availableRawPhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md)
  The pixel formats the capture output supports for RAW photo capture.
- [func supportedPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedphotopixelformattypes(for:).md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [func supportedRawPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedrawphotopixelformattypes(for:).md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [class func isAppleProRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isappleprorawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [class func isBayerRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isbayerrawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.
### Determining Supported Codec Types
- [var availablePhotoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablephotocodectypes.md)
  The compression codecs this capture output currently supports for photo capture.
- [func supportedPhotoCodecTypes(for: AVFileType) -> [AVVideoCodecType]](avcapturephotooutput/supportedphotocodectypes(for:).md)
  Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.
### Determining Supported File Types
- [var availablePhotoFileTypes: [AVFileType]](avcapturephotooutput/availablephotofiletypes.md)
  The list of file types currently supported for photo capture and output.
- [var availableRawPhotoFileTypes: [AVFileType]](avcapturephotooutput/availablerawphotofiletypes.md)
  The list of file types currently supported for RAW format capture and output.
### Suppressing the Shutter Sound
- [var isShutterSoundSuppressionSupported: Bool](avcapturephotooutput/isshuttersoundsuppressionsupported.md)
  A Boolean value that indicates whether the photo output supports suppressing the system shutter sound.
### Configuring ProRAW Support
- [var isAppleProRAWSupported: Bool](avcapturephotooutput/isappleprorawsupported.md)
  A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.
- [var isAppleProRAWEnabled: Bool](avcapturephotooutput/isappleprorawenabled.md)
  A Boolean value that indicates whether you’ve configured the photo output to deliver Apple ProRAW formats.
### Determining Available Settings
- [var isContentAwareDistortionCorrectionSupported: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isContentAwareDistortionCorrectionEnabled: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](avcapturephotooutput/maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](avcapturephotooutput/supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.
- [var isAutoRedEyeReductionSupported: Bool](avcapturephotooutput/isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.
### Monitoring the Visible Scene
- [var isFlashScene: Bool](avcapturephotooutput/isflashscene.md)
  A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.
- [var photoSettingsForSceneMonitoring: AVCapturePhotoSettings?](avcapturephotooutput/photosettingsforscenemonitoring.md)
  A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.
### Configuring High-Resolution Still Capture
- [var maxPhotoDimensions: CMVideoDimensions](avcapturephotooutput/maxphotodimensions.md)
  The maximum resolution of the requested photo.
### Configuring Live Photo Capture
- [var isLivePhotoCaptureSupported: Bool](avcapturephotooutput/islivephotocapturesupported.md)
  A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [var isLivePhotoCaptureEnabled: Bool](avcapturephotooutput/islivephotocaptureenabled.md)
  A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [var isLivePhotoCaptureSuspended: Bool](avcapturephotooutput/islivephotocapturesuspended.md)
  A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md)
  A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [var isLivePhotoAutoTrimmingEnabled: Bool](avcapturephotooutput/islivephotoautotrimmingenabled.md)
  A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [var availableLivePhotoVideoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablelivephotovideocodectypes.md)
  An array of video codecs currently available for Live Photo movie captures.
### Configuring Depth Data Capture
- [var isDepthDataDeliverySupported: Bool](avcapturephotooutput/isdepthdatadeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports depth data capture.
- [var isDepthDataDeliveryEnabled: Bool](avcapturephotooutput/isdepthdatadeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for depth data capture.
### Configuring Portrait Effects Matte Capture
- [var isPortraitEffectsMatteDeliveryEnabled: Bool](avcapturephotooutput/isportraiteffectsmattedeliveryenabled.md)
  A Boolean value indicating whether the capture output generates a portrait effects matte.
- [var isPortraitEffectsMatteDeliverySupported: Bool](avcapturephotooutput/isportraiteffectsmattedeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports delivery of a portrait effects matte.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](avcapturephoto/portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.
### Configuring Constant Color
- [var isConstantColorSupported: Bool](avcapturephotooutput/isconstantcolorsupported.md)
  A Boolean value that indicates whether a photo output supports constant color capture.
- [var isConstantColorEnabled: Bool](avcapturephotooutput/isconstantcolorenabled.md)
  A Boolean value that indicates whether the photo output configures the render pipeline to perform constant color capture.
### Configuring Virtual Device Capture
- [var isVirtualDeviceFusionSupported: Bool](avcapturephotooutput/isvirtualdevicefusionsupported.md)
  A Boolean value that indicates whether the device supports virtual device image fusion.
- [var isVirtualDeviceConstituentPhotoDeliverySupported: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.
- [var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md)
  A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.
### Preparing for Resource-Intensive Captures
- [var preparedPhotoSettingsArray: [AVCapturePhotoSettings]](avcapturephotooutput/preparedphotosettingsarray.md)
  An array of photo settings for which the photo output has prepared capture resources.
- [func setPreparedPhotoSettingsArray([AVCapturePhotoSettings], completionHandler: ((Bool, (any Error)?) -> Void)?)](avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:).md)
  Tells the photo capture output to prepare resources for future capture requests with the specified settings.
### Getting Segmentation Mattes
- [var availableSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](avcapturephotooutput/availablesemanticsegmentationmattetypes.md)
  An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.
- [var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](avcapturephotooutput/enabledsemanticsegmentationmattetypes.md)
  The semantic segmentation matte types that the photo render pipeline delivers.
### Setting the Capture Prioritization
- [var maxPhotoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](avcapturephotooutput/maxphotoqualityprioritization.md)
  The highest quality the photo output should prepare to deliver on a capture-by-capture basis.
- [AVCapturePhotoOutput.QualityPrioritization](avcapturephotooutput/qualityprioritization.md)
  Constants that indicate how to prioritize photo quality relative to capture speed.
### Determining Calibration Data Delivery Support
- [var isCameraCalibrationDataDeliverySupported: Bool](avcapturephotooutput/iscameracalibrationdatadeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports delivery of camera calibration data.
### Deprecated
- [Deprecated Symbols](avcapturephotooutput-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var availableRawPhotoCodecTypes: [AVVideoCodecType]](avcapturephotooutput/availablerawphotocodectypes.md)
### Instance Methods
- [func supportedRawPhotoCodecTypes(forRawPhotoPixelFormatType: OSType, fileType: AVFileType) -> [AVVideoCodecType]](avcapturephotooutput/supportedrawphotocodectypes(forrawphotopixelformattype:filetype:).md)

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
- [Capturing Still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](avcapturephoto.md)
  A container for image data from a photo capture output.
- [class AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [protocol AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md)
  Methods for monitoring progress and receiving results from a photo capture output.
- [class AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md)
  An object that monitors changes to a photo output’s capture readiness.
- [protocol AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md)
  A delegate protocol to receive updates about a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput)*