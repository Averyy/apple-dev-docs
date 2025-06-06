# keyboardMetrics

**Framework**: SensorKit  
**Kind**: property

A sensor that provides information about keyboard usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let keyboardMetrics: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRKeyboardMetrics`](srkeyboardmetrics.md).

You need to provide a reason to record keyboard metrics by adding the [`SRSensorUsageKeyboardMetrics`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageKeyboardMetrics) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let deviceUsageReport: SRSensor](srsensor/deviceusagereport.md)
  A sensor that provides information about device usage.
- [static let onWristState: SRSensor](srsensor/onwriststate.md)
  A sensor that describes the watch’s position on the wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)*