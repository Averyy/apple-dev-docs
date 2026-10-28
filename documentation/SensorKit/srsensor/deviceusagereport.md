# deviceUsageReport

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that provides information about device usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let deviceUsageReport: SRSensor
```

```c
extern SRSensor const SRSensorDeviceUsageReport;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`SRDeviceUsageReport`](../srdeviceusagereport.md).

You need to provide a reason to record the device usage by adding the [`SRSensorUsageDeviceUsage`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusagedeviceusage.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading device sensors
- [static let keyboardMetrics: SRSensor](./keyboardmetrics.md)
  A sensor that provides information about keyboard usage.
- [static let onWristState: SRSensor](./onwriststate.md)
  A sensor that describes the watch’s position on the wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/deviceusagereport)*