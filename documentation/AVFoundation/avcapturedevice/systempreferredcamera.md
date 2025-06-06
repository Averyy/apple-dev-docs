# systemPreferredCamera

**Framework**: AVFoundation  
**Kind**: property

A camera the system prefers to use for video and photo capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
class var systemPreferredCamera: AVCaptureDevice? { get }
```

#### Discussion

The system chooses the value of this property. It considers the value of [`userPreferredCamera`](avcapturedevice/userpreferredcamera.md), as well as other factors like camera suspension and the appearance of Continuity Cameras that apps should choose automatically. The property may change spontaneously, such as when the preferred camera goes away.

Apps that adopt this API should always key-value observe this property and update their capture session’s input device to reflect changes to this value. An app can still offer users the ability to pick a camera by setting a [`userPreferredCamera`](avcapturedevice/userpreferredcamera.md) value. Doing so puts the user’s choice first until either another system-preferred device becomes available or the user reboots the machine (after which it reverts to its original behavior of returning the internally-determined best camera to use).

If you want to offer users a fully manual camera selection mode in addition to automatic camera selection, it’s recommended to set the [`userPreferredCamera`](avcapturedevice/userpreferredcamera.md) value each time the user makes a camera selection, but ignore key-value observer updates to this property value while in manual selection mode.

This property always returns a device that’s present. If no camera is available, this value is `nil`.

## See Also

- [class var userPreferredCamera: AVCaptureDevice?](avcapturedevice/userpreferredcamera.md)
  A camera the user prefers to use for video and photo capture.
- [var isContinuityCamera: Bool](avcapturedevice/iscontinuitycamera.md)
  A Boolean value that indicates whether the device is a Continuity Camera.
- [var companionDeskViewCamera: AVCaptureDevice?](avcapturedevice/companiondeskviewcamera.md)
  A Desk View camera associated with a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempreferredcamera)*