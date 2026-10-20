# onWristState

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that describes the watch’s position on the wrist.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let onWristState: SRSensor
```

```c
extern SRSensor const SRSensorOnWristState;
```

#### Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`SRWristDetection`](../srwristdetection.md)

You need to provide a reason to detect the watch position by adding the [`SRSensorUsageWristDetection`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusagewristdetection.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading device sensors
- [static let deviceUsageReport: SRSensor](./deviceusagereport.md)
  A sensor that provides information about device usage.
- [static let keyboardMetrics: SRSensor](./keyboardmetrics.md)
  A sensor that provides information about keyboard usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/onwriststate)*