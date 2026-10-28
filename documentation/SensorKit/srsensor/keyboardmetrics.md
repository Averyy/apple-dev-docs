# keyboardMetrics

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that provides information about keyboard usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let keyboardMetrics: SRSensor
```

```c
extern SRSensor const SRSensorKeyboardMetrics;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`SRKeyboardMetrics`](../srkeyboardmetrics.md).

You need to provide a reason to record keyboard metrics by adding the [`SRSensorUsageKeyboardMetrics`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusagekeyboardmetrics.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading device sensors
- [static let deviceUsageReport: SRSensor](./deviceusagereport.md)
  A sensor that provides information about device usage.
- [static let onWristState: SRSensor](./onwriststate.md)
  A sensor that describes the watch’s position on the wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/keyboardmetrics)*