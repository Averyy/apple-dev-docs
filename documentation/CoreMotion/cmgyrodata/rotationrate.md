# rotationRate

**Framework**: Core Motion  
**Kind**: property

The rotation rate as measured by the device’s gyroscope.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rotationRate: CMRotationRate { get }
```

#### Discussion

This property yields a measurement of the device’s rate of rotation around three axes. Whereas this property gives the raw data from the gyroscope, the identically named property of [`CMDeviceMotion`](cmdevicemotion.md) gives a [`CMRotationRate`](cmrotationrate.md) structure measuring gyroscope data whose bias has been removed by Core Motion algorithms.

## See Also

- [Event Handling Guide for UIKit Apps](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)
- [struct CMRotationRate](cmrotationrate.md)
  The type of structures representing a measurement of rotation rate.
- [class CMRotationRateData](cmrotationratedata.md)
  A data object that contains a single rotation-rate measurement.
- [class CMRecordedRotationRateData](cmrecordedrotationratedata.md)
  A data object that contains a single rotation-rate measurement at a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmgyrodata/rotationrate)*