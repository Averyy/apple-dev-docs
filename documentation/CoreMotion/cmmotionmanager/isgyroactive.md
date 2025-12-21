# isGyroActive

**Framework**: Core Motion  
**Kind**: property

A Boolean value that determines whether gyroscope updates are currently happening.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isGyroActive: Bool { get }
```

#### Discussion

This property indicates whether [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) or [`startGyroUpdates()`](cmmotionmanager/startgyroupdates().md) has been called since the last time [`stopGyroUpdates()`](cmmotionmanager/stopgyroupdates().md) was called. (If the start methods hadn’t been called, the app could be getting updates from the gyroscope after calling, for example, [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md), but this property would return [`false`](https://developer.apple.com/documentation/Swift/false).)

## See Also

- [var isGyroAvailable: Bool](cmmotionmanager/isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.
- [var isDeviceMotionActive: Bool](cmmotionmanager/isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isAccelerometerActive: Bool](cmmotionmanager/isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isMagnetometerActive: Bool](cmmotionmanager/ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isgyroactive)*