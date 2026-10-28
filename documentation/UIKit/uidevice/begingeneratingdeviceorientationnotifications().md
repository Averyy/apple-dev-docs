# beginGeneratingDeviceOrientationNotifications()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Begins the generation of notifications of device orientation changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func beginGeneratingDeviceOrientationNotifications()
```

```objc
- (void) beginGeneratingDeviceOrientationNotifications;
```

## Discussion

You must call this method before attempting to get orientation data from the device. This method enables the device’s accelerometer hardware and begins the delivery of acceleration events to the device. The device subsequently uses these events to post [`orientationDidChangeNotification`](./orientationdidchangenotification.md) notifications when the device orientation changes and to update the [`orientation`](./orientation.md) property.

You may nest calls to this method safely, but you should always match each call with a corresponding call to the [`endGeneratingDeviceOrientationNotifications()`](./endgeneratingdeviceorientationnotifications%28%29.md) method.

## See Also

### Tracking the device orientation
- [var orientation: UIDeviceOrientation](./orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](../uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](./isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func endGeneratingDeviceOrientationNotifications()](./endgeneratingdeviceorientationnotifications%28%29.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/begingeneratingdeviceorientationnotifications())*