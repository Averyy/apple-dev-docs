# endGeneratingDeviceOrientationNotifications()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Ends the generation of notifications of device orientation changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func endGeneratingDeviceOrientationNotifications()
```

```objc
- (void) endGeneratingDeviceOrientationNotifications;
```

## Discussion

This method stops the posting of [`orientationDidChangeNotification`](./orientationdidchangenotification.md) notifications and notifies the system that it can power down the accelerometer hardware if it isn’t in use elsewhere. You call this method after a previous call to the [`beginGeneratingDeviceOrientationNotifications()`](./begingeneratingdeviceorientationnotifications%28%29.md) method.

## See Also

### Tracking the device orientation
- [var orientation: UIDeviceOrientation](./orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](../uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](./isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](./begingeneratingdeviceorientationnotifications%28%29.md)
  Begins the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/endgeneratingdeviceorientationnotifications())*