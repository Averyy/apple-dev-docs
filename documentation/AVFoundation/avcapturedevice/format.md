# AVCaptureDevice.Format

**Framework**: AVFoundation  
**Kind**: class

A class that defines media formats and capture settings that capture devices support.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class Format
```

#### Overview

A format object provides information about a media capture format to use with a capture device, such as video frame rates and zoom factors.

You can find more information about a capture format using its associated Core Media format description (see [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription)), available using the [`formatDescription`](avcapturedevice/format/formatdescription.md) property.

## Topics

### Determining Spatial Capture Support
- [var isSpatialVideoCaptureSupported: Bool](avcapturedevice/format/isspatialvideocapturesupported.md)
  A Boolean value that indicates whether the format supports capturing spatial video to a file.
### Determining Background Replacement Support
- [var isBackgroundReplacementSupported: Bool](avcapturedevice/format/isbackgroundreplacementsupported.md)
  A Boolean value that indicates whether the format supports background replacement.
- [var videoFrameRateRangeForBackgroundReplacement: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforbackgroundreplacement.md)
  The minimum and maximum frame rates available when Background Replacement is active.
### Determining Video Capture Support
- [var isAutoVideoFrameRateSupported: Bool](avcapturedevice/format/isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](avcapturedevice/format/videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [class AVFrameRateRange](avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoBinned: Bool](avcapturedevice/format/isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isVideoHDRSupported: Bool](avcapturedevice/format/isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](avcapturedevice/format/ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.
### Determining Reaction Effects Support
- [var reactionEffectsSupported: Bool](avcapturedevice/format/reactioneffectssupported.md)
  A Boolean value that indicates whether the device supports reaction effects.
- [var videoFrameRateRangeForReactionEffectsInProgress: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforreactioneffectsinprogress.md)
  Indicates the minimum and maximum frame rates available when a reaction effect runs.
### Determining Supported Media Formats
- [var mediaType: AVMediaType](avcapturedevice/format/mediatype.md)
  A constant describing the media type of an `AVCaptureDevice` active or supported format.
- [var formatDescription: CMFormatDescription](avcapturedevice/format/formatdescription.md)
  An object describing the capture format.
### Determining Output Support
- [var unsupportedCaptureOutputClasses: [AnyClass]](avcapturedevice/format/unsupportedcaptureoutputclasses.md)
  The list of capture output subclasses not allowed for capture with this format, if any.
### Determining Field of View
- [var videoFieldOfView: Float](avcapturedevice/format/videofieldofview.md)
  Indicates the format’s horizontal field of view in degrees.
- [var geometricDistortionCorrectedVideoFieldOfView: Float](avcapturedevice/format/geometricdistortioncorrectedvideofieldofview.md)
  A horizontal field of view for the format after correction for geometric distortion.
### Determining Video Stabilization Support
- [func isVideoStabilizationModeSupported(AVCaptureVideoStabilizationMode) -> Bool](avcapturedevice/format/isvideostabilizationmodesupported(_:).md)
  A Boolean value that indicates whether the format supports a given video stabilization mode.
- [enum AVCaptureVideoStabilizationMode](avcapturevideostabilizationmode.md)
  An enumeration of video stabilization modes that capture devices and formats support.
### Determining Photo Quality
- [var supportedMaxPhotoDimensions: [CMVideoDimensions]](avcapturedevice/format/supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.
- [var isHighPhotoQualitySupported: Bool](avcapturedevice/format/ishighphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [var isHighestPhotoQualitySupported: Bool](avcapturedevice/format/ishighestphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.
### Determining Color Support
- [var isGlobalToneMappingSupported: Bool](avcapturedevice/format/isglobaltonemappingsupported.md)
  A Boolean value that indicates whether the format supports global tone mapping.
- [var supportedColorSpaces: [AVCaptureColorSpace]](avcapturedevice/format/supportedcolorspaces.md)
  The list of the device’s supported color spaces.
### Determining Exposure Support
- [var systemRecommendedExposureBiasRange: ClosedRange<Float>?](avcapturedevice/format/systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [var minISO: Float](avcapturedevice/format/miniso.md)
  A floating-point number that indicates the minimum supported exposure ISO value.
- [var maxISO: Float](avcapturedevice/format/maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](avcapturedevice/format/minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.
- [var maxExposureDuration: CMTime](avcapturedevice/format/maxexposureduration.md)
  A time value that indicates the maximum supported exposure duration.
### Determining Zoom Capabilities
- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](avcapturedevice/format/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](avcapturedevice/format/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.
### Determining the Auto Focus System
- [var autoFocusSystem: AVCaptureDevice.Format.AutoFocusSystem](avcapturedevice/format/autofocussystem-swift.property.md)
  The auto focus system the format uses.
- [AVCaptureDevice.Format.AutoFocusSystem](avcapturedevice/format/autofocussystem-swift.enum.md)
  An enumeration of auto focus systems.
### Determining Center Stage Support
- [var isCenterStageSupported: Bool](avcapturedevice/format/iscenterstagesupported.md)
  A Boolean value that indicates whether the format supports Center Stage.
- [var videoFrameRateRangeForCenterStage: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcenterstage.md)
  The range of frame rates available when Center Stage is active.
- [var videoMinZoomFactorForCenterStage: CGFloat](avcapturedevice/format/videominzoomfactorforcenterstage.md)
  The minimum zoom factor available when Center Stage is active.
- [var videoMaxZoomFactorForCenterStage: CGFloat](avcapturedevice/format/videomaxzoomfactorforcenterstage.md)
  The maximum zoom factor available when Center Stage is active.
### Determining Portrait Effects Support
- [var isPortraitEffectSupported: Bool](avcapturedevice/format/isportraiteffectsupported.md)
  A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [var isPortraitEffectsMatteStillImageDeliverySupported: Bool](avcapturedevice/format/isportraiteffectsmattestillimagedeliverysupported.md)
  A Boolean indicating whether the device supports portrait matte effects in still-image capture.
- [var videoFrameRateRangeForPortraitEffect: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforportraiteffect.md)
  The range of frame rates available when Portrait Effect is active.
### Determining Studio Light Support
- [var isStudioLightSupported: Bool](avcapturedevice/format/isstudiolightsupported.md)
  A Boolean value that indicates whether the format supports Studio Light.
- [var videoFrameRateRangeForStudioLight: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforstudiolight.md)
  A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.
### Determinging Depth Capture Support
- [var supportedDepthDataFormats: [AVCaptureDevice.Format]](avcapturedevice/format/supporteddepthdataformats.md)
  The list of data formats compatible with this video format.
### Deprecated
- [Deprecated Symbols](avcapturedevice-format-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var defaultSimulatedAperture: Float](avcapturedevice/format/defaultsimulatedaperture.md)
- [var isCameraLensSmudgeDetectionSupported: Bool](avcapturedevice/format/iscameralenssmudgedetectionsupported.md)
- [var isCinematicVideoCaptureSupported: Bool](avcapturedevice/format/iscinematicvideocapturesupported.md)
- [var maxSimulatedAperture: Float](avcapturedevice/format/maxsimulatedaperture.md)
- [var minSimulatedAperture: Float](avcapturedevice/format/minsimulatedaperture.md)
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforcinematicvideo.md)
- [var videoMaxZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videomaxzoomfactorforcinematicvideo.md)
- [var videoMinZoomFactorForCinematicVideo: CGFloat](avcapturedevice/format/videominzoomfactorforcinematicvideo.md)

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

- [var formats: [AVCaptureDevice.Format]](avcapturedevice/formats.md)
  The capture formats a device supports.
- [var activeFormat: AVCaptureDevice.Format](avcapturedevice/activeformat.md)
  The capture format in use by the device.
- [var activeDepthDataFormat: AVCaptureDevice.Format?](avcapturedevice/activedepthdataformat.md)
  The currently active depth data format of the capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format)*