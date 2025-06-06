# White Balance

**Framework**: AVFoundation

Configure the automatic white balance behavior of a camera, or manually control white balance settings.

## Topics

### Configuring Automatic White Balance
- [func isWhiteBalanceModeSupported(AVCaptureDevice.WhiteBalanceMode) -> Bool](avcapturedevice/iswhitebalancemodesupported(_:).md)
  Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.property.md)
  The current white balance mode.
- [AVCaptureDevice.WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.enum.md)
  Constants to specify the white balance mode of a capture device.
### Monitoring White Balance Changes
- [var isAdjustingWhiteBalance: Bool](avcapturedevice/isadjustingwhitebalance.md)
  A Boolean value that indicates whether the device is currently adjusting the white balance.
### Inspecting Gain Levels
- [var deviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains.md)
  The current device-specific RGB white balance gain values in use.
- [var grayWorldDeviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](avcapturedevice/grayworlddevicewhitebalancegains.md)
  The current device-specific white balance values required for a neutral gray white point.
- [var maxWhiteBalanceGain: Float](avcapturedevice/maxwhitebalancegain.md)
  The maximum supported value to which you can set a color channel.
### Performing Conversions
- [func chromaticityValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/chromaticityvalues(for:).md)
  Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/temperatureandtintvalues(for:).md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-3wtsa.md)
  Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](avcapturedevice/whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.
### Setting White Balance Manually
- [var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool](avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.md)
  A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [func setWhiteBalanceModeLocked(with: AVCaptureDevice.WhiteBalanceGains, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setwhitebalancemodelocked(with:completionhandler:).md)
  Sets the white balance to locked mode with the specified white balance gains.

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
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-white-balance)*