# isDeviceMotionAvailable

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isDeviceMotionAvailable) BOOL deviceMotionAvailable;
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

#### Discussion

The device-motion service is available if a device has both an accelerometer and a gyroscope. Because all devices have accelerometers, this property is functionally equivalent to [`isGyroAvailable`](./isgyroavailable.md).

## See Also

### Related Documentation
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)
  A Boolean value that determines whether the app is receiving updates from the device-motion service.
### Determining the Availability of Services
- [var isAccelerometerAvailable: Bool](./isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
- [var isGyroAvailable: Bool](./isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.
- [var isMagnetometerAvailable: Bool](./ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isdevicemotionavailable)*