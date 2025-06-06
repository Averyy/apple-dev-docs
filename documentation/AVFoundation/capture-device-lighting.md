# Lighting

**Framework**: AVFoundation

Configure the device flash, torch, and low light settings.

## Topics

### Configuring Flash Settings
- [var hasFlash: Bool](avcapturedevice/hasflash.md)
  A Boolean value that indicates whether the capture device has a flash.
- [var isFlashAvailable: Bool](avcapturedevice/isflashavailable.md)
  A Boolean value that indicates whether the flash is currently available for use.
- [var isFlashActive: Bool](avcapturedevice/isflashactive.md)
  A Boolean value that indicates whether the flash is currently active.
- [var flashMode: AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.property.md)
  The device’s current flash mode.
- [func isFlashModeSupported(AVCaptureDevice.FlashMode) -> Bool](avcapturedevice/isflashmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the given flash mode.
- [AVCaptureDevice.FlashMode](avcapturedevice/flashmode-swift.enum.md)
  Constants that specify the flash modes of a capture device.
### Configuring Torch Settings
- [var hasTorch: Bool](avcapturedevice/hastorch.md)
  A Boolean value that specifies whether the capture device has a torch.
- [var isTorchAvailable: Bool](avcapturedevice/istorchavailable.md)
  A Boolean value that indicates whether the torch is currently available for use.
- [var isTorchActive: Bool](avcapturedevice/istorchactive.md)
  A Boolean value that indicates whether the device’s torch is currently active.
- [var torchLevel: Float](avcapturedevice/torchlevel.md)
  The current torch brightness level.
- [var torchMode: AVCaptureDevice.TorchMode](avcapturedevice/torchmode-swift.property.md)
  The current torch mode.
- [AVCaptureDevice.TorchMode](avcapturedevice/torchmode-swift.enum.md)
  Constants to specify the capture device’s torch mode.
- [func isTorchModeSupported(AVCaptureDevice.TorchMode) -> Bool](avcapturedevice/istorchmodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [func setTorchModeOn(level: Float) throws](avcapturedevice/settorchmodeon(level:).md)
  Sets the illumination level when in torch mode.
- [class let maxAvailableTorchLevel: Float](avcapturedevice/maxavailabletorchlevel.md)
  A constant that indicates to set the torch to its maximum level.
### Configuring Low Light Settings
- [var isLowLightBoostSupported: Bool](avcapturedevice/islowlightboostsupported.md)
  A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.
- [var isLowLightBoostEnabled: Bool](avcapturedevice/islowlightboostenabled.md)
  A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.
- [var automaticallyEnablesLowLightBoostWhenAvailable: Bool](avcapturedevice/automaticallyenableslowlightboostwhenavailable.md)
  A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.

## See Also

- [func lockForConfiguration() throws](avcapturedevice/lockforconfiguration.md)
  Requests exclusive access to configure device hardware properties.
- [func unlockForConfiguration()](avcapturedevice/unlockforconfiguration.md)
  Releases exclusive control over device hardware properties.
- [var isSubjectAreaChangeMonitoringEnabled: Bool](avcapturedevice/issubjectareachangemonitoringenabled.md)
  A Boolean value that indicates whether the device monitors the subject area for changes.
- [class let subjectAreaDidChangeNotification: NSNotification.Name](avcapturedevice/subjectareadidchangenotification.md)
  A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](capture-device-formats.md)
  Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md)
  Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md)
  Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White Balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-lighting)*