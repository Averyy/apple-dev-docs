# setExposureModeCustom(duration:iso:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setExposureModeCustom(duration: CMTime, iso ISO: Float, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

```swift
func setExposureModeCustom(duration: CMTime, iso ISO: Float) async -> CMTime
```

```objc
- (void) setExposureModeCustomWithDuration:(CMTime) duration ISO:(float) ISO completionHandler:(void (^)(CMTime syncTime)) handler;
```

## Discussion

This method throws an exception if you set the exposure duration or ISO values to an unsupported level

Before changing exposure mode, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

When using [`AVCapturePhotoOutput`](../avcapturephotooutput.md) to capture photos, the [`photoQualityPrioritization`](../avcapturephotosettings/photoqualityprioritization.md) property of [`AVCapturePhotoSettings`](../avcapturephotosettings.md) defaults to [`AVCapturePhotoOutput.QualityPrioritization.balanced`](../avcapturephotooutput/qualityprioritization/balanced.md), which allows photo capture to temporarily override the capture device’s exposure duration and ISO if the scene is dark enough to require multi-image fusion to improve quality. To ensure that the system honors the device exposure duration and ISO values while in [`AVCaptureDevice.ExposureMode.custom`](./exposuremode-swift.enum/custom.md) or [`AVCaptureDevice.ExposureMode.locked`](./exposuremode-swift.enum/locked.md) mode, you must photo quality prioritization to [`AVCapturePhotoOutput.QualityPrioritization.speed`](../avcapturephotooutput/qualityprioritization/speed.md).

## Parameters

- `duration`: The exposure duration.

  Pass a value of [`currentExposureDuration`](./currentexposureduration.md) to leave the current exposure duration unchanged.

  Changes made to the exposure duration may result in changes to [`activeVideoMinFrameDuration`](./activevideominframeduration.md) or [`activeVideoMaxFrameDuration`](./activevideomaxframeduration.md).
- `ISO`: The exposure ISO value.

  Pass a value of [`currentISO`](./currentiso.md) to leave the current ISO unchanged.
- `handler`: A callback the system invokes when the adjustment to the exposure duration and ISO is complete. If you call this method multiple times, the system calls the completion handlers in FIFO order.

  The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md).

  You can pass `nil` for this parameter if you don’t require this information.

## Topics

### Exposure constants
- [class let currentExposureDuration: CMTime](./currentexposureduration.md)
  A special constant representing the current exposure duration setting.
- [class let currentISO: Float](./currentiso.md)
  A constant to indicate not to specify a new ISO value, and instead set it to its current value.

## See Also

### Configuring exposure manually
- [func setExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md)
  Sets a custom exposure mode with the specified lens aperture, exposure duration, and ISO values.
- [class let autoExposureDuration: CMTime](./autoexposureduration.md)
  A special value that may be passed as the duration parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the exposure duration.
- [class let autoISO: Float](./autoiso.md)
  A special value that may be passed as the ISO parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the gain value.
- [class let autoLensAperture: Float](./autolensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the aperture.
- [class let currentLensAperture: Float](./currentlensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to lock at the current position.
- [var exposureDuration: CMTime](./exposureduration.md)
  The length of time over which exposure takes place.
- [var iso: Float](./iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](./lensaperture.md)
  The size of the lens diaphragm.
- [var activeMaxExposureDuration: CMTime](./activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var automaticallyAdjustsExposureDuration: Bool](./automaticallyadjustsexposureduration.md)
  This property reports true whenever exposureDuration is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureExposureDurationAuto` to the duration parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var automaticallyAdjustsISO: Bool](./automaticallyadjustsiso.md)
  This property reports true whenever ISO is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureISOAuto` to the ISO parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var automaticallyAdjustsLensAperture: Bool](./automaticallyadjustslensaperture.md)
  This property reports true whenever lensAperture is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureLensApertureAuto` to the aperture parameter of [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var autoExposureLensApertureRateLimit: Float](./autoexposurelensapertureratelimit.md)
  Specifies a rate limit for aperture motion, whenever auto-exposure is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:))*