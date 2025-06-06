# userPreferredCamera

**Framework**: Avfoundation  
**Kind**: property

A camera the user prefers to use for video and photo capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
class var userPreferredCamera: AVCaptureDevice? { get set }
```

#### Discussion

In addition to being a [`systemPreferredCamera`](avcapturedevice/systempreferredcamera.md), you can designate a device as a user-preferred camera. Setting a value for this property allows an app to persist its preference across app launches and system reboots. The system internally maintains a short history of devices, so if a user’s most recently preferred camera isn’t currently connected, it still reports the next best choice.

This property always returns a device that’s present. If no camera is available, this value is `nil`.

> **Note**:  Setting the value to `nil` has no effect.

## See Also

- [class var systemPreferredCamera: AVCaptureDevice?](avcapturedevice/systempreferredcamera.md)
  A camera the system prefers to use for video and photo capture.
- [var isContinuityCamera: Bool](avcapturedevice/iscontinuitycamera.md)
  A Boolean value that indicates whether the device is a Continuity Camera.
- [var companionDeskViewCamera: AVCaptureDevice?](avcapturedevice/companiondeskviewcamera.md)
  A Desk View camera associated with a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/userpreferredcamera)*