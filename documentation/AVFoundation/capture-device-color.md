# Color

**Framework**: AVFoundation

Manage HDR and color space settings for a device.

## Topics

### Configuring HDR Settings
- [var automaticallyAdjustsVideoHDREnabled: Bool](avcapturedevice/automaticallyadjustsvideohdrenabled.md)
  A Boolean value that indicates whether the device automatically manages the state of high dynamic range (HDR) video streaming.
- [var isVideoHDREnabled: Bool](avcapturedevice/isvideohdrenabled.md)
  A Boolean value that indicates whether the device streams high dynamic range video buffers, also known as extended dynamic range (EDR).
### Enabling Global Tone Mapping
- [var isGlobalToneMappingEnabled: Bool](avcapturedevice/isglobaltonemappingenabled.md)
  A Boolean value that indicates whether the device should use global tone mapping.
### Configuring Color Space Settings
- [var activeColorSpace: AVCaptureColorSpace](avcapturedevice/activecolorspace.md)
  The currently active color space for capture.
- [enum AVCaptureColorSpace](avcapturecolorspace.md)
  An enumeration of color spaces a device can support.

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
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-color)*