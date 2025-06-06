# endGeneratingDeviceOrientationNotifications()

**Framework**: UIKit  
**Kind**: method

Ends the generation of notifications of device orientation changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func endGeneratingDeviceOrientationNotifications()
```

#### Discussion

This method stops the posting of [`orientationDidChangeNotification`](uidevice/orientationdidchangenotification.md) notifications and notifies the system that it can power down the accelerometer hardware if it isn’t in use elsewhere. You call this method after a previous call to the [`beginGeneratingDeviceOrientationNotifications()`](uidevice/begingeneratingdeviceorientationnotifications().md) method.

## See Also

- [var orientation: UIDeviceOrientation](uidevice/orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](uidevice/isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](uidevice/begingeneratingdeviceorientationnotifications.md)
  Begins the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/endgeneratingdeviceorientationnotifications())*