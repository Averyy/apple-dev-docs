# phoneUsageReport

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that reports the amount of time that the user is on phone calls.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let phoneUsageReport: SRSensor
```

```c
extern SRSensor const SRSensorPhoneUsageReport;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is [`SRPhoneUsageReport`](../srphoneusagereport.md).

You need to provide a reason to record phone usage by adding the [`SRSensorUsagePhoneUsage`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusagephoneusage.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading app activity sensors
- [static let messagesUsageReport: SRSensor](./messagesusagereport.md)
  A sensor that provides information about use of the Messages app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)*