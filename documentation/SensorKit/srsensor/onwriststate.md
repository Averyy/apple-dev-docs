# onWristState

**Framework**: SensorKit  
**Kind**: property

A sensor that describes the watch’s position on the wrist.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let onWristState: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRWristDetection`](srwristdetection.md)

You need to provide a reason to detect the watch position by adding the [`SRSensorUsageWristDetection`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageWristDetection) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let deviceUsageReport: SRSensor](srsensor/deviceusagereport.md)
  A sensor that provides information about device usage.
- [static let keyboardMetrics: SRSensor](srsensor/keyboardmetrics.md)
  A sensor that provides information about keyboard usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)*