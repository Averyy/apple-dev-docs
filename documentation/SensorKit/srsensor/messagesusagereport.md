# messagesUsageReport

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that provides information about use of the Messages app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let messagesUsageReport: SRSensor
```

```c
extern SRSensor const SRSensorMessagesUsageReport;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`SRMessagesUsageReport`](../srmessagesusagereport.md).

You need to provide a reason to record Messages app usage by adding the [`SRSensorUsageMessageUsage`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusagemessageusage.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading app activity sensors
- [static let phoneUsageReport: SRSensor](./phoneusagereport.md)
  A sensor that reports the amount of time that the user is on phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)*