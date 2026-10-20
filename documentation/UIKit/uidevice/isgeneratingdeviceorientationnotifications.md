# isGeneratingDeviceOrientationNotifications

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device generates orientation notifications.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isGeneratingDeviceOrientationNotifications: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isGeneratingDeviceOrientationNotifications) BOOL generatesDeviceOrientationNotifications;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the shared [`UIDevice`](../uidevice.md) object posts a [`orientationDidChangeNotification`](./orientationdidchangenotification.md) notification when the device changes orientation. If the value is [`false`](../../Swift/false.md), it generates no orientation notifications. Device orientation notifications can only be generated between calls to the [`beginGeneratingDeviceOrientationNotifications()`](./begingeneratingdeviceorientationnotifications%28%29.md) and [`endGeneratingDeviceOrientationNotifications()`](./endgeneratingdeviceorientationnotifications%28%29.md) methods.

## See Also

### Tracking the device orientation
- [var orientation: UIDeviceOrientation](./orientation.md)
  The physical orientation of the device.
- [enum UIDeviceOrientation](../uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [func beginGeneratingDeviceOrientationNotifications()](./begingeneratingdeviceorientationnotifications%28%29.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](./endgeneratingdeviceorientationnotifications%28%29.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/isgeneratingdeviceorientationnotifications)*