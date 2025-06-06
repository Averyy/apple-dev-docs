# orientation

**Framework**: UIKit  
**Kind**: property

The physical orientation of the device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var orientation: UIDeviceOrientation { get }
```

#### Discussion

The value of the property is a constant that indicates the current orientation of the device. This value represents the physical orientation of the device and may be different from the current orientation of your application’s user interface. See [`UIDeviceOrientation`](uideviceorientation.md) for descriptions of the possible values.

The value of this property always returns 0 unless orientation notifications have been enabled by calling [`beginGeneratingDeviceOrientationNotifications()`](uidevice/begingeneratingdeviceorientationnotifications().md).

## See Also

- [enum UIDeviceOrientation](uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](uidevice/isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](uidevice/begingeneratingdeviceorientationnotifications.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](uidevice/endgeneratingdeviceorientationnotifications.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/orientation)*