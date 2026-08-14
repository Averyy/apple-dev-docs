# automaticallyEnablesLowLightBoostWhenAvailable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var automaticallyEnablesLowLightBoostWhenAvailable: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). When it’s [`true`](https://developer.apple.com/documentation/swift/true), the device may engage a special low-light boost mode to improve image quality. It switches, at its discretion, to a special boost mode under low light, and back to normal operation when the scene becomes sufficiently lit.

Setting a value for this property throws an exception if the value of [`isLowLightBoostSupported`](avcapturedevice/islowlightboostsupported.md) is false.

A capture device that supports this feature may only engage boost mode for certain source formats or resolutions. The switch between normal operation and low light boost mode may drop one or more video frames.

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

- [var isLowLightBoostSupported: Bool](avcapturedevice/islowlightboostsupported.md)
  A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.
- [var isLowLightBoostEnabled: Bool](avcapturedevice/islowlightboostenabled.md)
  A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyenableslowlightboostwhenavailable)*