# isDeviceMotionAvailable

**Framework**: Core Motion  
**Kind**: property

A Boolean value that indicates whether the device-motion service is available on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isDeviceMotionAvailable: Bool { get }
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

The device-motion service is available if a device has both an accelerometer and a gyroscope. Because all devices have accelerometers, this property is functionally equivalent to [`isGyroAvailable`](cmmotionmanager/isgyroavailable.md).

## See Also

- [var isDeviceMotionActive: Bool](cmmotionmanager/isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
- [var isAccelerometerAvailable: Bool](cmmotionmanager/isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
- [var isGyroAvailable: Bool](cmmotionmanager/isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.
- [var isMagnetometerAvailable: Bool](cmmotionmanager/ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)*