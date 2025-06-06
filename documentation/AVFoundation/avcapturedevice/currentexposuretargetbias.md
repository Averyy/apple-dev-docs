# currentExposureTargetBias

**Framework**: AVFoundation  
**Kind**: property

A special constant that represents the current exposure bias value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let currentExposureTargetBias: Float
```

#### Discussion

Pass this value to the [`setExposureTargetBias(_:completionHandler:)`](avcapturedevice/setexposuretargetbias(_:completionhandler:).md) method to lock exposure bias to its current value, which disables autoexposure.

## See Also

- [var exposureTargetOffset: Float](avcapturedevice/exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var exposureTargetBias: Float](avcapturedevice/exposuretargetbias.md)
  The bias to apply to the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](avcapturedevice/minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](avcapturedevice/maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [func setExposureTargetBias(Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuretargetbias(_:completionhandler:).md)
  Sets the bias to apply to the target exposure value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentexposuretargetbias)*