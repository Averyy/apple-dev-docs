# autoLensAperture

**Framework**: AVFoundation  
**Kind**: property

A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the aperture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```swift
class let autoLensAperture: Float
```

#### Discussion

This value may be passed to [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md) to enable “priority” modes, where some parameters are locked to specified values (given “priority”), whereas the ones specified as “auto” will be continually adjusted by the system to maintain image brightness.

## See Also

- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [func setExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md)
  Sets a custom exposure mode with the specified lens aperture, exposure duration, and ISO values.
- [class let autoExposureDuration: CMTime](avcapturedevice/autoexposureduration.md)
  A special value that may be passed as the duration parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the exposure duration.
- [class let autoISO: Float](avcapturedevice/autoiso.md)
  A special value that may be passed as the ISO parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the gain value.
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
- [var autoExposureLensApertureRateLimit: Float](avcapturedevice/autoexposurelensapertureratelimit.md)
  Specifies a rate limit for aperture motion, whenever auto-exposure is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autolensaperture)*