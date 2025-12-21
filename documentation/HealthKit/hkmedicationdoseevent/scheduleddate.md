# scheduledDate

**Framework**: HealthKit  
**Kind**: property

The date and time the person takes the medication, if scheduled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var scheduledDate: Date? { get }
```

#### Discussion

The value is always non-null for [`HKMedicationDoseEvent.ScheduleType.schedule`](hkmedicationdoseevent/scheduletype-swift.enum/schedule.md) and always null for  [`HKMedicationDoseEvent.ScheduleType.asNeeded`](hkmedicationdoseevent/scheduletype-swift.enum/asneeded.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/scheduleddate)*