# HKMedicationDoseEvent.LogStatus

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKMedicationDoseEventLogStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [HKMedicationDoseEvent.LogStatus.notInteracted](./logstatus-swift.enum/notinteracted.md)
  The person doesn’t interact with a scheduled medication reminder.
- [HKMedicationDoseEvent.LogStatus.notLogged](./logstatus-swift.enum/notlogged.md)
  The person undoes a previously logged medication status.
- [HKMedicationDoseEvent.LogStatus.notificationNotSent](./logstatus-swift.enum/notificationnotsent.md)
  The system assigns this status when it fails to deliver a scheduled medication notification.
- [HKMedicationDoseEvent.LogStatus.skipped](./logstatus-swift.enum/skipped.md)
  The person logs that they skipped the medication dose.
- [HKMedicationDoseEvent.LogStatus.snoozed](./logstatus-swift.enum/snoozed.md)
  The person snoozes a scheduled medication notification.
- [HKMedicationDoseEvent.LogStatus.taken](./logstatus-swift.enum/taken.md)
  The person logs that they took the medication dose.
### Initializers
- [init?(rawValue: Int)](./logstatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/logstatus-swift.enum)*