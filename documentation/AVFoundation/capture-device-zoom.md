# Zoom

**Framework**: AVFoundation

Configure device zooming behavior and inspect hardware capabilities.

## Topics

### Adjusting Zoom
- [var videoZoomFactor: CGFloat](avcapturedevice/videozoomfactor.md)
  A value that controls the cropping and enlargement of images captured by the device.
- [func ramp(toVideoZoomFactor: CGFloat, withRate: Float)](avcapturedevice/ramp(tovideozoomfactor:withrate:).md)
  Begins a smooth transition from the current zoom factor to another.
- [func cancelVideoZoomRamp()](avcapturedevice/cancelvideozoomramp.md)
  Smoothly ends a zoom transition in progress.
### Observing Zoom
- [var isRampingVideoZoom: Bool](avcapturedevice/isrampingvideozoom.md)
  A Boolean value that indicates whether a zoom transition is in progress.
### Inspecting Zoom Factors
- [var minAvailableVideoZoomFactor: CGFloat](avcapturedevice/minavailablevideozoomfactor.md)
  The minimum zoom factor allowed in the current capture configuration.
- [var maxAvailableVideoZoomFactor: CGFloat](avcapturedevice/maxavailablevideozoomfactor.md)
  The maximum zoom factor allowed in the current capture configuration.
- [var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber]](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md)
  An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [var dualCameraSwitchOverVideoZoomFactor: CGFloat](avcapturedevice/dualcameraswitchovervideozoomfactor.md)
  The video zoom factor at which a dual camera device can automatically switch between cameras.
- [var displayVideoZoomFactorMultiplier: CGFloat](avcapturedevice/displayvideozoomfactormultiplier.md)
  A video zoom factor multiplier to use when displaying zoom information in a user interface.
### Enabling Geometric Distortion Correction
- [var isGeometricDistortionCorrectionSupported: Bool](avcapturedevice/isgeometricdistortioncorrectionsupported.md)
  A Boolean value that indicates whether this device supports geometric distortion correction.
- [var isGeometricDistortionCorrectionEnabled: Bool](avcapturedevice/isgeometricdistortioncorrectionenabled.md)
  A Boolean value that indicates whether geometric distortion correction is enabled for this device.

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
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-zoom)*