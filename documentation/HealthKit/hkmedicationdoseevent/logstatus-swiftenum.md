# HKMedicationDoseEvent.LogStatus

**Framework**: HealthKit  
**Kind**: enum

The statuses the system assigns to a logged medication dose event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum LogStatus
```

## Topics

### Enumeration Cases
- [HKMedicationDoseEvent.LogStatus.notInteracted](hkmedicationdoseevent/logstatus-swift.enum/notinteracted.md)
  The person doesn’t interact with a scheduled medication reminder.
- [HKMedicationDoseEvent.LogStatus.notLogged](hkmedicationdoseevent/logstatus-swift.enum/notlogged.md)
  The person undoes a previously logged medication status.
- [HKMedicationDoseEvent.LogStatus.notificationNotSent](hkmedicationdoseevent/logstatus-swift.enum/notificationnotsent.md)
  The system assigns this status when it fails to deliver a scheduled medication notification.
- [HKMedicationDoseEvent.LogStatus.skipped](hkmedicationdoseevent/logstatus-swift.enum/skipped.md)
  The person logs that they skipped the medication dose.
- [HKMedicationDoseEvent.LogStatus.snoozed](hkmedicationdoseevent/logstatus-swift.enum/snoozed.md)
  The person snoozes a scheduled medication notification.
- [HKMedicationDoseEvent.LogStatus.taken](hkmedicationdoseevent/logstatus-swift.enum/taken.md)
  The person logs that they took the medication dose.
### Initializers
- [init?(rawValue: Int)](hkmedicationdoseevent/logstatus-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/logstatus-swift.enum)*