# scheduleType

**Framework**: HealthKit  
**Kind**: property

The scheduling context for this logged dose event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var scheduleType: HKMedicationDoseEvent.ScheduleType { get }
```

#### Discussion

The system sets this to [`HKMedicationDoseEvent.ScheduleType.asNeeded`](hkmedicationdoseevent/scheduletype-swift.enum/asneeded.md) when the person logs a dose without a schedule and [`HKMedicationDoseEvent.ScheduleType.schedule`](hkmedicationdoseevent/scheduletype-swift.enum/schedule.md) when a person logs a dose from a scheduled medication reminder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/scheduletype-swift.property)*