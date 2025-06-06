# isSubjectAreaChangeMonitoringEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the device monitors the subject area for changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isSubjectAreaChangeMonitoringEnabled: Bool { get set }
```

#### Discussion

The value of this property indicates whether the device monitors the video subject area for changes, such as lighting changes, substantial movement, and so on. If you enable subject area change monitoring, the capture device object sends an [`subjectAreaDidChangeNotification`](avcapturedevice/subjectareadidchangenotification.md) whenever it detects a change to the subject area. You can observe this notification and take action such as focusing, adjusting exposure, and so on.

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re finished configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [func lockForConfiguration() throws](avcapturedevice/lockforconfiguration.md)
  Requests exclusive access to configure device hardware properties.
- [func unlockForConfiguration()](avcapturedevice/unlockforconfiguration.md)
  Releases exclusive control over device hardware properties.
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
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/issubjectareachangemonitoringenabled)*