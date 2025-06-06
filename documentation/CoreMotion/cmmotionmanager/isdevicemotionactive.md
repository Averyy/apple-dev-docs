# isDeviceMotionActive

**Framework**: Core Motion  
**Kind**: property

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

#### Discussion

This property indicates whether [`startDeviceMotionUpdates(to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md) or [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md) has been called since the last time [`stopDeviceMotionUpdates()`](cmmotionmanager/stopdevicemotionupdates().md) was called.

## See Also

- [var isDeviceMotionAvailable: Bool](cmmotionmanager/isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
- [var isAccelerometerActive: Bool](cmmotionmanager/isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isGyroActive: Bool](cmmotionmanager/isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.
- [var isMagnetometerActive: Bool](cmmotionmanager/ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionactive)*