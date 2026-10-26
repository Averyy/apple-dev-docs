# AVCaptureDevice.Format

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptureDeviceFormat : NSObject
```

## Mentions

- [Adopting smart framing in your camera app](../adopting-smart-framing-in-your-camera-app.md)

#### Overview

A format object provides information about a media capture format to use with a capture device, such as video frame rates and zoom factors.

You can find more information about a capture format using its associated Core Media format description (see [`CMFormatDescription`](../../CoreMedia/cmformatdescription.md)), available using the [`formatDescription`](./format/formatdescription.md) property.

## Topics

### Determining spatial capture support
- [var isSpatialVideoCaptureSupported: Bool](./format/isspatialvideocapturesupported.md)
  A Boolean value that indicates whether the format supports capturing spatial video to a file.
### Determining background replacement support
- [var isBackgroundReplacementSupported: Bool](./format/isbackgroundreplacementsupported.md)
  A Boolean value that indicates whether the format supports background replacement.
- [var videoFrameRateRangeForBackgroundReplacement: AVFrameRateRange?](./format/videoframeraterangeforbackgroundreplacement.md)
  The minimum and maximum frame rates available when Background Replacement is active.
### Determining video capture support
- [var isAutoVideoFrameRateSupported: Bool](./format/isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](./format/videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [class AVFrameRateRange](../avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoBinned: Bool](./format/isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isVideoHDRSupported: Bool](./format/isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](./format/ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.
### Determining reaction effects support
- [var reactionEffectsSupported: Bool](./format/reactioneffectssupported.md)
  A Boolean value that indicates whether the device supports reaction effects.
- [var videoFrameRateRangeForReactionEffectsInProgress: AVFrameRateRange?](./format/videoframeraterangeforreactioneffectsinprogress.md)
  Indicates the minimum and maximum frame rates available when a reaction effect runs.
### Determining supported media formats
- [var mediaType: AVMediaType](./format/mediatype.md)
  A constant describing the media type of an `AVCaptureDevice` active or supported format.
- [var formatDescription: CMFormatDescription](./format/formatdescription.md)
  An object describing the capture format.
### Determining output support
- [var unsupportedCaptureOutputClasses: [AnyClass]](./format/unsupportedcaptureoutputclasses.md)
  The list of capture output subclasses not allowed for capture with this format, if any.
### Determining field of view
- [var videoFieldOfView: Float](./format/videofieldofview.md)
  Indicates the format’s horizontal field of view in degrees.
- [var geometricDistortionCorrectedVideoFieldOfView: Float](./format/geometricdistortioncorrectedvideofieldofview.md)
  A horizontal field of view for the format after correction for geometric distortion.
### Determining video stabilization support
- [func isVideoStabilizationModeSupported(AVCaptureVideoStabilizationMode) -> Bool](./format/isvideostabilizationmodesupported%28_%29.md)
  A Boolean value that indicates whether the format supports a given video stabilization mode.
- [enum AVCaptureVideoStabilizationMode](../avcapturevideostabilizationmode.md)
  An enumeration of video stabilization modes that capture devices and formats support.
### Determining photo quality
- [var supportedMaxPhotoDimensions: [CMVideoDimensions]](./format/supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.
- [var isHighPhotoQualitySupported: Bool](./format/ishighphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [var isHighestPhotoQualitySupported: Bool](./format/ishighestphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.
- [supportedMaxPhotoDimensions](../avcapturedeviceformat/supportedmaxphotodimensions.md)
  The maximum photo dimension this format supports.
### Determining color support
- [var isGlobalToneMappingSupported: Bool](./format/isglobaltonemappingsupported.md)
  A Boolean value that indicates whether the format supports global tone mapping.
- [var supportedColorSpaces: [AVCaptureColorSpace]](./format/supportedcolorspaces.md)
  The list of the device’s supported color spaces.
- [supportedColorSpaces](../avcapturedeviceformat/supportedcolorspaces.md)
  The list of color spaces the format supports for image and video capture.
### Determining exposure support
- [var systemRecommendedExposureBiasRange: ClosedRange<Float>?](./format/systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [var minISO: Float](./format/miniso.md)
  A floating-point number that indicates the minimum supported exposure ISO value.
- [var maxISO: Float](./format/maxiso.md)
  A floating-point number that indicates the maximum supported exposure ISO value.
- [var minExposureDuration: CMTime](./format/minexposureduration.md)
  A time value that indicates the minimum supported exposure duration.
- [var maxExposureDuration: CMTime](./format/maxexposureduration.md)
  A time value that indicates the maximum supported exposure duration.
- [systemRecommendedExposureBiasRange](../avcapturedeviceformat/systemrecommendedexposurebiasrange.md)
  The system’s recommended exposure bias range for this device format.
- [AVExposureBiasRange](../avexposurebiasrange.md)
  An object that expresses an inclusive range of supported exposure bias values, in EV units.
### Determining zoom capabilities
- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](./format/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](./format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](./format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](./format/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](./format/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](./format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.
- [systemRecommendedVideoZoomRange](../avcapturedeviceformat/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [secondaryNativeResolutionZoomFactors](../avcapturedeviceformat/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](../avcapturedeviceformat/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [AVZoomRange](../avzoomrange.md)
  An object that defines an inclusive range of zoom values.
### Determining the auto focus system
- [var autoFocusSystem: AVCaptureDevice.Format.AutoFocusSystem](./format/autofocussystem-swift.property.md)
  The auto focus system the format uses.
- [AVCaptureDevice.Format.AutoFocusSystem](./format/autofocussystem-swift.enum.md)
  An enumeration of auto focus systems.
### Determining Cinematic video support
- [var isCinematicVideoCaptureSupported: Bool](./format/iscinematicvideocapturesupported.md)
  Indicates whether the format supports Cinematic Video capture.
- [var defaultSimulatedAperture: Float](./format/defaultsimulatedaperture.md)
  Default shallow depth of field simulated aperture.
- [var minSimulatedAperture: Float](./format/minsimulatedaperture.md)
  Minimum supported shallow depth of field simulated aperture.
- [var maxSimulatedAperture: Float](./format/maxsimulatedaperture.md)
  Maximum supported shallow depth of field simulated aperture.
- [var videoMaxZoomFactorForCinematicVideo: CGFloat](./format/videomaxzoomfactorforcinematicvideo.md)
  Indicates the maximum zoom factor available for the [`videoZoomFactor`](./videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoMinZoomFactorForCinematicVideo: CGFloat](./format/videominzoomfactorforcinematicvideo.md)
  Indicates the minimum zoom factor available for the [`videoZoomFactor`](./videozoomfactor.md) property when Cinematic Video capture is enabled on the device input.
- [var videoFrameRateRangeForCinematicVideo: AVFrameRateRange?](./format/videoframeraterangeforcinematicvideo.md)
  Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.
### Determining lens smudge detection support
- [var isCameraLensSmudgeDetectionSupported: Bool](./format/iscameralenssmudgedetectionsupported.md)
  Whether camera lens smudge detection is supported.
### Determining smart framing support
- [var isSmartFramingSupported: Bool](./format/issmartframingsupported.md)
  Returns `true` if smart framing is supported by the current format.
### Determining dynamic aspect ratio support
- [var supportedDynamicAspectRatios: [AVCaptureDevice.AspectRatio]](./format/supporteddynamicaspectratios.md)
  Indicates the supported aspect ratios for the device format.
- [func videoFieldOfView(for: AVCaptureDevice.AspectRatio, geometricDistortionCorrected: Bool) -> Float](./format/videofieldofview%28for,geometricdistortioncorrected%29.md)
  Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.
### Determining Center Stage support
- [var isCenterStageSupported: Bool](./format/iscenterstagesupported.md)
  A Boolean value that indicates whether the format supports Center Stage.
- [var videoFrameRateRangeForCenterStage: AVFrameRateRange?](./format/videoframeraterangeforcenterstage.md)
  The range of frame rates available when Center Stage is active.
- [var videoMinZoomFactorForCenterStage: CGFloat](./format/videominzoomfactorforcenterstage.md)
  The minimum zoom factor available when Center Stage is active.
- [var videoMaxZoomFactorForCenterStage: CGFloat](./format/videomaxzoomfactorforcenterstage.md)
  The maximum zoom factor available when Center Stage is active.
### Determining Portrait Effects support
- [var isPortraitEffectSupported: Bool](./format/isportraiteffectsupported.md)
  A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [var isPortraitEffectsMatteStillImageDeliverySupported: Bool](./format/isportraiteffectsmattestillimagedeliverysupported.md)
  A Boolean indicating whether the device supports portrait matte effects in still-image capture.
- [var videoFrameRateRangeForPortraitEffect: AVFrameRateRange?](./format/videoframeraterangeforportraiteffect.md)
  The range of frame rates available when Portrait Effect is active.
### Determining Studio Light support
- [var isStudioLightSupported: Bool](./format/isstudiolightsupported.md)
  A Boolean value that indicates whether the format supports Studio Light.
- [var videoFrameRateRangeForStudioLight: AVFrameRateRange?](./format/videoframeraterangeforstudiolight.md)
  A value that indicates the minimum and maximum frame rates available when a user enables Studio Light.
### Determining depth capture support
- [var supportedDepthDataFormats: [AVCaptureDevice.Format]](./format/supporteddepthdataformats.md)
  The list of data formats compatible with this video format.
- [var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat]](./format/supportedvideozoomfactorsfordepthdatadelivery.md)
  The zoom factors that a format supports for depth data delivery.
### Deprecated
- [Deprecated symbols](../avcapturedevice-format-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var defaultLensAperture: Float](./format/defaultlensaperture.md)
  The default value for the [`lensAperture`](./lensaperture.md) property.
- [var isCinematicVideoMetadataCaptureSupported: Bool](./format/iscinematicvideometadatacapturesupported.md)
  Indicates whether the format supports Cinematic Video Metadata capture.
- [var isContinuousAutoFocusTrackingSupported: Bool](./format/iscontinuousautofocustrackingsupported.md)
  Indicates whether the device format supports continuous autofocus tracking.
- [var isEdgeLightSupported: Bool](./format/isedgelightsupported.md)
  Indicates whether the format supports the Edge Light feature.
- [var isLowLightVideoNoiseReductionSupported: Bool](./format/islowlightvideonoisereductionsupported.md)
  Indicates whether the format supports low light video noise reduction.
- [var maxLensAperture: Float](./format/maxlensaperture.md)
  The maximum supported value for the [`lensAperture`](./lensaperture.md) property.
- [var minLensAperture: Float](./format/minlensaperture.md)
  The minimum supported value for the [`lensAperture`](./lensaperture.md) property.
- [var recommendedLensApertureStops: [Float]](./format/recommendedlensaperturestops.md)
- [recommendedLensApertureStops](../avcapturedeviceformat/recommendedlensaperturestops.md)
  A sorted array of recommended values for the [`lensAperture`](./lensaperture.md) property.
- [supportedVideoZoomFactorsForDepthDataDelivery](../avcapturedeviceformat/supportedvideozoomfactorsfordepthdatadelivery.md)
  The zoom factors that a format supports for depth data delivery.
### Instance Methods
- [func supportsExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float) -> Bool](./format/supportsexposuremodecustom%28lensaperture,duration,iso%29.md)
  Reports if the given set of exposure parameters are supported by this format.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring capture formats
- [var formats: [AVCaptureDevice.Format]](./formats.md)
  The capture formats a device supports.
- [var activeFormat: AVCaptureDevice.Format](./activeformat.md)
  The capture format in use by the device.
- [var activeDepthDataFormat: AVCaptureDevice.Format?](./activedepthdataformat.md)
  The currently active depth data format of the capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format)*