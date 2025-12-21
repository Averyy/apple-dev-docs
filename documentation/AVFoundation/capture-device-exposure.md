# Exposure

**Framework**: AVFoundation

Configure the automatic exposure behavior of a camera, or manually control its exposure settings.

## Topics

### Managing the exposure mode
- [func isExposureModeSupported(AVCaptureDevice.ExposureMode) -> Bool](avcapturedevice/isexposuremodesupported(_:).md)
  Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [var exposureMode: AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.property.md)
  The exposure mode for the device.
- [AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.enum.md)
  Constants that specify the exposure mode of a capture device.
### Setting an exposure point of interest
- [var isExposurePointOfInterestSupported: Bool](avcapturedevice/isexposurepointofinterestsupported.md)
  A Boolean value that indicates whether the device supports a point of interest for exposure.
- [var exposurePointOfInterest: CGPoint](avcapturedevice/exposurepointofinterest.md)
  The point of interest for exposure.
### Setting an exposure rectangle of interest
- [var isExposureRectOfInterestSupported: Bool](avcapturedevice/isexposurerectofinterestsupported.md)
  Whether the device supports exposure rectangles of interest.
- [var exposureRectOfInterest: CGRect](avcapturedevice/exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [var minExposureRectOfInterestSize: CGSize](avcapturedevice/minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForExposurePoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforexposurepoint(ofinterest:).md)
  The default rectangle of interest used for a given exposure point of interest.
### Configuring face-driven automatic exposure
- [var isFaceDrivenAutoExposureEnabled: Bool](avcapturedevice/isfacedrivenautoexposureenabled.md)
  A Boolean value that indicates whether the device has face-driven autoexposure enabled.
- [var automaticallyAdjustsFaceDrivenAutoExposureEnabled: Bool](avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.md)
  A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.
### Monitoring exposure changes
- [var isAdjustingExposure: Bool](avcapturedevice/isadjustingexposure.md)
  A Boolean value that indicates whether the device is currently adjusting its exposure setting.
### Adjusting exposure compensation
- [var exposureTargetOffset: Float](avcapturedevice/exposuretargetoffset.md)
  The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [var exposureTargetBias: Float](avcapturedevice/exposuretargetbias.md)
  The bias to apply to the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](avcapturedevice/minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](avcapturedevice/maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](avcapturedevice/currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.
- [func setExposureTargetBias(Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuretargetbias(_:completionhandler:).md)
  Sets the bias to apply to the target exposure value.
### Configuring exposure manually
- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var activeMaxExposureDuration: CMTime](avcapturedevice/activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.
- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.

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
- [White balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capture-device-exposure)*