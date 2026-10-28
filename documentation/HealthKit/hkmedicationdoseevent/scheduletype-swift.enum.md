# HKMedicationDoseEvent.ScheduleType

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKMedicationDoseEventScheduleType : NSInteger;
```

## Overview

Each value tells you whether the person logged the dose ad-hoc or in response to a scheduled medication reminder.

## Topics

### Enumeration Cases
- [HKMedicationDoseEvent.ScheduleType.asNeeded](./scheduletype-swift.enum/asneeded.md)
  The person logged this dose event ad-hoc, outside of any scheduled reminder.
- [HKMedicationDoseEvent.ScheduleType.schedule](./scheduletype-swift.enum/schedule.md)
  The person logged this dose event in response to a scheduled medication reminder.
### Initializers
- [init?(rawValue: Int)](./scheduletype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/scheduletype-swift.enum)*