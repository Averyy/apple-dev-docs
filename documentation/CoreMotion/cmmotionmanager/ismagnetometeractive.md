# isMagnetometerActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isMagnetometerActive) BOOL magnetometerActive;
```

## Discussion

This property indicates whether the [`startMagnetometerUpdates(to:withHandler:)`](./startmagnetometerupdates%28to,withhandler%29.md) or [`startMagnetometerUpdates()`](./startmagnetometerupdates%28%29.md) method has been called since the last time the [`stopMagnetometerUpdates()`](./stopmagnetometerupdates%28%29.md) method was called. (If the start methods hadn’t been called, the app could be getting updates from the magnetometer after calling, for example, [`startDeviceMotionUpdates()`](./startdevicemotionupdates%28%29.md), but this property would return [`false`](../../Swift/false.md).)

## See Also

### Related Documentation
- [var isMagnetometerAvailable: Bool](./ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.
### Determining Which Services Are Active
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
- [var isGyroActive: Bool](./isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeractive)*