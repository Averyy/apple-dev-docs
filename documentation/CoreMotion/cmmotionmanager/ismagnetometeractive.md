# isMagnetometerActive

**Framework**: Core Motion  
**Kind**: property

A Boolean value that determines whether magnetometer updates are currently happening.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
var isMagnetometerActive: Bool { get }
```

#### Discussion

This property indicates whether the [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) or [`startMagnetometerUpdates()`](cmmotionmanager/startmagnetometerupdates().md) method has been called since the last time the [`stopMagnetometerUpdates()`](cmmotionmanager/stopmagnetometerupdates().md) method was called. (If the start methods hadn’t been called, the app could be getting updates from the magnetometer after calling, for example, [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md), but this property would return [`false`](https://developer.apple.com/documentation/Swift/false).)

## See Also

- [var isMagnetometerAvailable: Bool](cmmotionmanager/ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.
- [var isDeviceMotionActive: Bool](cmmotionmanager/isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isAccelerometerActive: Bool](cmmotionmanager/isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isGyroActive: Bool](cmmotionmanager/isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)*