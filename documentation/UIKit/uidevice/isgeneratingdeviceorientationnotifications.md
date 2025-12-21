# isGeneratingDeviceOrientationNotifications

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the device generates orientation notifications.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isGeneratingDeviceOrientationNotifications: Bool { get }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the shared [`UIDevice`](uidevice.md) object posts a [`orientationDidChangeNotification`](uidevice/orientationdidchangenotification.md) notification when the device changes orientation. If the value is [`false`](https://developer.apple.com/documentation/Swift/false), it generates no orientation notifications. Device orientation notifications can only be generated between calls to the [`beginGeneratingDeviceOrientationNotifications()`](uidevice/begingeneratingdeviceorientationnotifications().md) and [`endGeneratingDeviceOrientationNotifications()`](uidevice/endgeneratingdeviceorientationnotifications().md) methods.

## See Also

- [var orientation: UIDeviceOrientation](uidevice/orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [func beginGeneratingDeviceOrientationNotifications()](uidevice/begingeneratingdeviceorientationnotifications.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](uidevice/endgeneratingdeviceorientationnotifications.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isgeneratingdeviceorientationnotifications)*