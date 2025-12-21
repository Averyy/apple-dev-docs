# setExposureModeCustom(duration:iso:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setExposureModeCustom(duration: CMTime, iso ISO: Float) async -> CMTime
```

#### Discussion

This method throws an exception if you set the exposure duration or ISO values to an unsupported level

Before changing exposure mode, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

When using [`AVCapturePhotoOutput`](avcapturephotooutput.md) to capture photos, the [`photoQualityPrioritization`](avcapturephotosettings/photoqualityprioritization.md) property of [`AVCapturePhotoSettings`](avcapturephotosettings.md) defaults to [`AVCapturePhotoOutput.QualityPrioritization.balanced`](avcapturephotooutput/qualityprioritization/balanced.md), which allows photo capture to temporarily override the capture device’s exposure duration and ISO if the scene is dark enough to require multi-image fusion to improve quality. To ensure that the system honors the device exposure duration and ISO values while in [`AVCaptureDevice.ExposureMode.custom`](avcapturedevice/exposuremode-swift.enum/custom.md) or [`AVCaptureDevice.ExposureMode.locked`](avcapturedevice/exposuremode-swift.enum/locked.md) mode, you must photo quality prioritization to [`AVCapturePhotoOutput.QualityPrioritization.speed`](avcapturephotooutput/qualityprioritization/speed.md).

## Parameters

- `duration`: Changes made to the exposure duration may result in changes to   or  .
- `ISO`: Pass a value of   to leave the current ISO unchanged.
- `handler`: You can pass   for this parameter if you don’t require this information.

## Topics

### Exposure constants
- [class let currentExposureDuration: CMTime](avcapturedevice/currentexposureduration.md)
  A special constant representing the current exposure duration setting.
- [class let currentISO: Float](avcapturedevice/currentiso.md)
  A constant to indicate not to specify a new ISO value, and instead set it to its current value.

## See Also

- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var activeMaxExposureDuration: CMTime](avcapturedevice/activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:))*