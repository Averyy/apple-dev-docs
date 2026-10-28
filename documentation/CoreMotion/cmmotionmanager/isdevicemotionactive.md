# isDeviceMotionActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the app is receiving updates from the device-motion service.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isDeviceMotionActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDeviceMotionActive) BOOL deviceMotionActive;
```

## Discussion

This property indicates whether [`startDeviceMotionUpdates(to:withHandler:)`](./startdevicemotionupdates%28to,withhandler%29.md) or [`startDeviceMotionUpdates()`](./startdevicemotionupdates%28%29.md) has been called since the last time [`stopDeviceMotionUpdates()`](./stopdevicemotionupdates%28%29.md) was called.

## See Also

### Related Documentation
- [var isDeviceMotionAvailable: Bool](./isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
### Determining Which Services Are Active
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isGyroActive: Bool](./isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.
- [var isMagnetometerActive: Bool](./ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)*