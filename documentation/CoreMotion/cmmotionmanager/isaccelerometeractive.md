# isAccelerometerActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isAccelerometerActive) BOOL accelerometerActive;
```

## Discussion

This property indicates whether [`startAccelerometerUpdates(to:withHandler:)`](./startaccelerometerupdates%28to,withhandler%29.md) or [`startAccelerometerUpdates()`](./startaccelerometerupdates%28%29.md) has been called since the last time [`stopAccelerometerUpdates()`](./stopaccelerometerupdates%28%29.md) was called. (If the start methods hadn’t been called, the app could be getting updates from the accelerometer after calling, for example, [`startDeviceMotionUpdates()`](./startdevicemotionupdates%28%29.md), but this property would return [`false`](../../Swift/false.md).)

## See Also

### Related Documentation
- [var isAccelerometerAvailable: Bool](./isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
### Determining Which Services Are Active
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isGyroActive: Bool](./isgyroactive.md)
  A Boolean value that determines whether gyroscope updates are currently happening.
- [var isMagnetometerActive: Bool](./ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeractive)*