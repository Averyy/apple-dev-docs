# isMagnetometerAvailable

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a magnetometer is available on the device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
var isMagnetometerAvailable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMagnetometerAvailable) BOOL magnetometerAvailable;
```

## See Also

### Related Documentation
- [var isMagnetometerActive: Bool](./ismagnetometeractive.md)
  A Boolean value that determines whether magnetometer updates are currently happening.
### Determining the Availability of Services
- [var isDeviceMotionAvailable: Bool](./isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
- [var isAccelerometerAvailable: Bool](./isaccelerometeravailable.md)
  A Boolean value that indicates whether an accelerometer is available on the device.
- [var isGyroAvailable: Bool](./isgyroavailable.md)
  A Boolean value that indicates whether a gyroscope is available on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/ismagnetometeravailable)*