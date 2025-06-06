# messagesUsageReport

**Framework**: SensorKit  
**Kind**: property

A sensor that provides information about use of the Messages app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let messagesUsageReport: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRMessagesUsageReport`](srmessagesusagereport.md).

You need to provide a reason to record Messages app usage by adding the [`SRSensorUsageMessageUsage`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMessageUsage) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail) key in the information property list.

## See Also

- [static let phoneUsageReport: SRSensor](srsensor/phoneusagereport.md)
  A sensor that reports the amount of time that the user is on phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/messagesusagereport)*