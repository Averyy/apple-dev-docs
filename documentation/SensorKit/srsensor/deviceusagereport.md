# deviceUsageReport

**Framework**: SensorKit  
**Kind**: property

A sensor that provides information about device usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let deviceUsageReport: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRDeviceUsageReport`](srdeviceusagereport.md).

You need to provide a reason to record the device usage by adding the [`SRSensorUsageDeviceUsage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageDeviceUsage) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let keyboardMetrics: SRSensor](srsensor/keyboardmetrics.md)
  A sensor that provides information about keyboard usage.
- [static let onWristState: SRSensor](srsensor/onwriststate.md)
  A sensor that describes the watch’s position on the wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)*