# isAccelerometerActive

**Framework**: Core Motion  
**Kind**: property

A Boolean value that indicates whether accelerometer updates are currently happening.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isAccelerometerActive: Bool { get }
```

#### Discussion

This property indicates whether [`startAccelerometerUpdates(to:withHandler:)`](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md) or [`startAccelerometerUpdates()`](cmmotionmanager/startaccelerometerupdates().md) has been called since the last time [`stopAccelerometerUpdates()`](cmmotionmanager/stopaccelerometerupdates().md) was called. (If the start methods hadn’t been called, the app could be getting updates from the accelerometer after calling, for example, [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md), but this property would return [`false`](https://developer.apple.com/documentation/swift/false).)

## See Also

- [var isAccelerometerAvailable: Bool](cmmotionmanager/isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
- [var isDeviceMotionActive: Bool](cmmotionmanager/isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isGyroActive: Bool](cmmotionmanager/isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.
- [var isMagnetometerActive: Bool](cmmotionmanager/ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)*