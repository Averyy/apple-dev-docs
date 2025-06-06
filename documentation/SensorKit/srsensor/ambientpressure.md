# ambientPressure

**Framework**: SensorKit  
**Kind**: property

A sensor that provides pressure and temperature metrics.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static let ambientPressure: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is `[`[`CMRecordedPressureData`](https://developer.apple.com/documentation/CoreMotion/CMRecordedPressureData)`]`.

You need to provide a reason to record ambient pressure by adding the [`SRSensorUsageElevation`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageElevation) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let ambientLightSensor: SRSensor](srsensor/ambientlightsensor.md)
  A sensor that provides ambient light information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure)*