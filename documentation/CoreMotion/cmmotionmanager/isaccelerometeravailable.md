# isAccelerometerAvailable

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an accelerometer is available on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isAccelerometerAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAccelerometerAvailable) BOOL accelerometerAvailable;
```

## Mentions

- [Getting raw accelerometer events](../getting-raw-accelerometer-events.md)

## See Also

### Related Documentation
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)
  A Boolean value that indicates whether accelerometer updates are currently happening.
### Determining the Availability of Services
- [var isDeviceMotionAvailable: Bool](./isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
- [var isGyroAvailable: Bool](./isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.
- [var isMagnetometerAvailable: Bool](./ismagnetometeravailable.md)
  A Boolean value that indicates whether a magnetometer is available on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/isaccelerometeravailable)*