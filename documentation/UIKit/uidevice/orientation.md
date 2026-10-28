# orientation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The physical orientation of the device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var orientation: UIDeviceOrientation { get }
```

```objc
@property (nonatomic, readonly) UIDeviceOrientation orientation;
```

## Discussion

The value of the property is a constant that indicates the current orientation of the device. This value represents the physical orientation of the device and may be different from the current orientation of your application’s user interface. See [`UIDeviceOrientation`](../uideviceorientation.md) for descriptions of the possible values.

The value of this property always returns 0 unless orientation notifications have been enabled by calling [`beginGeneratingDeviceOrientationNotifications()`](./begingeneratingdeviceorientationnotifications%28%29.md).

## See Also

### Tracking the device orientation
- [enum UIDeviceOrientation](../uideviceorientation.md)
  Constants that describe the physical orientation of the device.
- [var isGeneratingDeviceOrientationNotifications: Bool](./isgeneratingdeviceorientationnotifications.md)
  A Boolean value that indicates whether the device generates orientation notifications.
- [func beginGeneratingDeviceOrientationNotifications()](./begingeneratingdeviceorientationnotifications%28%29.md)
  Begins the generation of notifications of device orientation changes.
- [func endGeneratingDeviceOrientationNotifications()](./endgeneratingdeviceorientationnotifications%28%29.md)
  Ends the generation of notifications of device orientation changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/orientation)*