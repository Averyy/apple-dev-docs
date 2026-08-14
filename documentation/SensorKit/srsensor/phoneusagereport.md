# phoneUsageReport

**Framework**: SensorKit  
**Kind**: property

A sensor that reports the amount of time that the user is on phone calls.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let phoneUsageReport: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRPhoneUsageReport`](srphoneusagereport.md).

You need to provide a reason to record phone usage by adding the [`SRSensorUsagePhoneUsage`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail/srsensorusagephoneusage) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail) key in the information property list.

## See Also

- [static let messagesUsageReport: SRSensor](srsensor/messagesusagereport.md)
  A sensor that provides information about use of the Messages app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/phoneusagereport)*