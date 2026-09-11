# autoExposureLensApertureRateLimit

**Framework**: AVFoundation  
**Kind**: property

Specifies a rate limit for aperture motion, whenever auto-exposure is active.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
var autoExposureLensApertureRateLimit: Float { get set }
```

#### Discussion

This rate limit is enforced whenever the auto-exposure system has control of one or more exposure parameters, to ensure smooth transitions between target values with coordinated management of the automatically adjusted parameters to maintain image brightness. However, if a full set of explicit (not “auto”) positions are passed to `setExposureModeCustomWithLensAperture:duration:ISO:completionHandler:`, any change to aperture is immediately applied without rate limit. In this case, the client has full control of the exposure parameters, and can implement arbitrary exposure transitions by repeated calls to the setter.

This value limits the maximum frame-to-frame change of aperture size, as the ratio of aperture area between consecutive frames. For example, a value of 1.1 limits the aperture to accepting 10% additional light on each consecutive frame (or reducing by 10% when closing). A value of 1.0 does not allow any aperture motion. A special value of 0 (the default) allows the system to adjust the aperture speed automatically, such as faster motion in preview and slower when recording. When assigned to a value other than 0, the value must be greater than or equal to 1.0.

> **Note**: `NSGenericException` if assigned without first obtaining exclusive access to the receiver using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).

## See Also

- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [func setExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md)
  Sets a custom exposure mode with the specified lens aperture, exposure duration, and ISO values.
- [class let autoExposureDuration: CMTime](avcapturedevice/autoexposureduration.md)
  A special value that may be passed as the duration parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the exposure duration.
- [class let autoISO: Float](avcapturedevice/autoiso.md)
  A special value that may be passed as the ISO parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the gain value.
- [class let autoLensAperture: Float](avcapturedevice/autolensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the aperture.
- [class let currentLensAperture: Float](avcapturedevice/currentlensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to lock at the current position.
- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.
- [var activeMaxExposureDuration: CMTime](avcapturedevice/activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var automaticallyAdjustsExposureDuration: Bool](avcapturedevice/automaticallyadjustsexposureduration.md)
  This property reports true whenever exposureDuration is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureExposureDurationAuto` to the duration parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).
- [var automaticallyAdjustsISO: Bool](avcapturedevice/automaticallyadjustsiso.md)
  This property reports true whenever ISO is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureISOAuto` to the ISO parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).
- [var automaticallyAdjustsLensAperture: Bool](avcapturedevice/automaticallyadjustslensaperture.md)
  This property reports true whenever lensAperture is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureLensApertureAuto` to the aperture parameter of [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autoexposurelensapertureratelimit)*