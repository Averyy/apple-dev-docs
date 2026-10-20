# exposureTargetBias

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) float exposureTargetBias;
```

## Mentions

- [Enhancing your app experience with the Camera Control](../enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

When the device exposure mode is [`AVCaptureDevice.ExposureMode.continuousAutoExposure`](./exposuremode-swift.enum/continuousautoexposure.md) or [`AVCaptureDevice.ExposureMode.locked`](./exposuremode-swift.enum/locked.md), the bias affects both metering ([`exposureTargetOffset`](./exposuretargetoffset.md)), and the actual exposure level ([`exposureDuration`](./exposureduration.md) and [`iso`](./iso.md)).  When the exposure mode is [`AVCaptureDevice.ExposureMode.custom`](./exposuremode-swift.enum/custom.md), it only affects metering.

This property is key-value observable.

## See Also

### Adjusting exposure compensation
- [var exposureTargetOffset: Float](./exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](./minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](./maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](./currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.
- [func setExposureTargetBias(Float, completionHandler: ((CMTime) -> Void)?)](./setexposuretargetbias%28_,completionhandler%29.md)
  Sets the bias to apply to the target exposure value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuretargetbias)*