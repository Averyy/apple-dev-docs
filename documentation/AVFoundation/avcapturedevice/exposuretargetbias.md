# exposureTargetBias

**Framework**: AVFoundation  
**Kind**: property

The bias to apply to the target exposure value, in exposure value (EV) units.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var exposureTargetBias: Float { get }
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

When the device exposure mode is [`AVCaptureDevice.ExposureMode.continuousAutoExposure`](avcapturedevice/exposuremode-swift.enum/continuousautoexposure.md) or [`AVCaptureDevice.ExposureMode.locked`](avcapturedevice/exposuremode-swift.enum/locked.md), the bias affects both metering ([`exposureTargetOffset`](avcapturedevice/exposuretargetoffset.md)), and the actual exposure level ([`exposureDuration`](avcapturedevice/exposureduration.md) and [`iso`](avcapturedevice/iso.md)).  When the exposure mode is [`AVCaptureDevice.ExposureMode.custom`](avcapturedevice/exposuremode-swift.enum/custom.md), it only affects metering.

This property is key-value observable.

## See Also

- [var exposureTargetOffset: Float](avcapturedevice/exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](avcapturedevice/minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](avcapturedevice/maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](avcapturedevice/currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.
- [func setExposureTargetBias(Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuretargetbias(_:completionhandler:).md)
  Sets the bias to apply to the target exposure value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuretargetbias)*