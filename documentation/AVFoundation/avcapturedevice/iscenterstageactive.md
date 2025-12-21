# isCenterStageActive

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether Center Stage is active on a device.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
var isCenterStageActive: Bool { get }
```

#### Discussion

When Center Stage is active, the camera automatically pans, tightens, or widens the field of view as it requires to keep people optimally framed. If an app or a user enables Center Stage, this property value is [`true`](https://developer.apple.com/documentation/Swift/true) if the device supports the feature in its current configuration.

The system imposes the following restrictions on a device when Center Stage is active:

- It limits the range of values the device supports for its [`minAvailableVideoZoomFactor`](avcapturedevice/minavailablevideozoomfactor.md) and [`maxAvailableVideoZoomFactor`](avcapturedevice/maxavailablevideozoomfactor.md) properties to those of the active capture format’s [`videoMinZoomFactorForCenterStage`](avcapturedevice/format/videominzoomfactorforcenterstage.md) and [`videoMaxZoomFactorForCenterStage`](avcapturedevice/format/videomaxzoomfactorforcenterstage.md), respectively.
- It limits the [`activeVideoMinFrameDuration`](avcapturedevice/activevideominframeduration.md) and [`activeVideoMaxFrameDuration`](avcapturedevice/activevideomaxframeduration.md) to the value set by the active capture format’s [`videoFrameRateRangeForCenterStage`](avcapturedevice/format/videoframeraterangeforcenterstage.md) property.

The system deactivates Center Stage in the following cases:

- You enable depth data delivery on a capture output, such as [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) or [`AVCapturePhotoOutput`](avcapturephotooutput.md).
- The device supports geometric distortion correction, but you haven’t enabled it by setting the value of [`isGeometricDistortionCorrectionEnabled`](avcapturedevice/isgeometricdistortioncorrectionenabled.md) to [`true`](https://developer.apple.com/documentation/Swift/true).

This property is key-value observable.

## See Also

- [class var isCenterStageEnabled: Bool](avcapturedevice/iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](avcapturedevice/centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.
- [AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscenterstageactive)*