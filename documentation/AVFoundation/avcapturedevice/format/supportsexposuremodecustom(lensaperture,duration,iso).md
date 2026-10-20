# supportsExposureModeCustom(lensAperture:duration:iso:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Reports if the given set of exposure parameters are supported by this format.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
func supportsExposureModeCustom(lensAperture: Float, duration: CMTime, iso ISO: Float) -> Bool
```

```objc
- (BOOL) supportsExposureModeCustomWithLensAperture:(float) lensAperture duration:(CMTime) duration ISO:(float) ISO;
```

#### Discussion

The intended use of this method is to query which combinations of “Auto” parameters (`AVFCapture/AVCaptureLensApertureAuto`, `AVFCapture/AVCaptureExposureDurationAuto`, `AVFCapture/AVCaptureISOAuto`) are supported by this format. If you pass a numeric constant it will be range checked against the parameter’s supported min and max. However you can also pass the “Current” constants (`AVFCapture/AVCaptureLensApertureCurrent`, `AVFCapture/AVCaptureExposureDurationCurrent`, `AVFCapture/AVCaptureISOCurrent`) to generically query locked vs. auto parameter support without picking arbitrary lock values.

> **Example**: To query support for “shutter priority” where the exposure duration is locked but auto-exposure continues to manage aperture and ISO:
>
> ```swift
> format.supportsExposureModeCustom(lensAperture: AVCaptureDevice.autoLensAperture, duration: AVCaptureDevice.currentExposureDuration, iso: AVCaptureDevice.autoISO)
> ```

Devices that have fixed aperture will have equivalent support for `AVFCapture/AVCaptureLensApertureAuto` and `AVFCapture/AVCaptureLensApertureCurrent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supportsexposuremodecustom(lensaperture:duration:iso:))*