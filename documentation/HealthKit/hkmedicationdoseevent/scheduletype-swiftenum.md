# HKMedicationDoseEvent.ScheduleType

**Framework**: HealthKit  
**Kind**: enum

The kind of schedule the system associates with a logged medication dose event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum ScheduleType
```

#### Overview

Each value tells you whether the person logged the dose ad-hoc or in response to a scheduled medication reminder.

## Topics

### Enumeration Cases
- [HKMedicationDoseEvent.ScheduleType.asNeeded](hkmedicationdoseevent/scheduletype-swift.enum/asneeded.md)
  The person logged this dose event ad-hoc, outside of any scheduled reminder.
- [HKMedicationDoseEvent.ScheduleType.schedule](hkmedicationdoseevent/scheduletype-swift.enum/schedule.md)
  The person logged this dose event in response to a scheduled medication reminder.
### Initializers
- [init?(rawValue: Int)](hkmedicationdoseevent/scheduletype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/scheduletype-swift.enum)*