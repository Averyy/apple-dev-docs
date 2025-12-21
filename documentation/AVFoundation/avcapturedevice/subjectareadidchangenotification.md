# subjectAreaDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property

A notification the system posts when a capture device detects a substantial change to the video subject area.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let subjectAreaDidChangeNotification: NSNotification.Name
```

#### Discussion

The system posts this notification only if the device’s [`isSubjectAreaChangeMonitoringEnabled`](avcapturedevice/issubjectareachangemonitoringenabled.md) property value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func lockForConfiguration() throws](avcapturedevice/lockforconfiguration.md)
  Requests exclusive access to configure device hardware properties.
- [func unlockForConfiguration()](avcapturedevice/unlockforconfiguration.md)
  Releases exclusive control over device hardware properties.
- [var isSubjectAreaChangeMonitoringEnabled: Bool](avcapturedevice/issubjectareachangemonitoringenabled.md)
  A Boolean value that indicates whether the device monitors the subject area for changes.
- [Formats](capture-device-formats.md)
  Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md)
  Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md)
  Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](capture-device-white-balance.md)
  Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md)
  Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md)
  Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md)
  Configure device zooming behavior and inspect hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/subjectareadidchangenotification)*