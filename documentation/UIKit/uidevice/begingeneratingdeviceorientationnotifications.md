# beginGeneratingDeviceOrientationNotifications()

**Framework**: UIKit  
**Kind**: method

Begins the generation of notifications of device orientation changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func beginGeneratingDeviceOrientationNotifications()
```

#### Discussion

You must call this method before attempting to get orientation data from the device. This method enables the device’s accelerometer hardware and begins the delivery of acceleration events to the device. The device subsequently uses these events to post [`orientationDidChangeNotification`](uidevice/orientationdidchangenotification.md) notifications when the device orientation changes and to update the [`orientation`](uidevice/orientation.md) property.

You may nest calls to this method safely, but you should always match each call with a corresponding call to the [`endGeneratingDeviceOrientationNotifications()`](uidevice/endgeneratingdeviceorientationnotifications().md) method.

## See Also

- [var orientation: UIDeviceOrientation](uidevice/orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](uidevice/isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func endGeneratingDeviceOrientationNotifications()](uidevice/endgeneratingdeviceorientationnotifications.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/begingeneratingdeviceorientationnotifications())*