# scheduledDoseQuantity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The dose quantity a person is expected to take based on their medication schedule.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * scheduledDoseQuantity;
```

## Discussion

The value is always non-null for [`HKMedicationDoseEvent.ScheduleType.schedule`](./scheduletype-swift.enum/schedule.md), and always null for [`HKMedicationDoseEvent.ScheduleType.asNeeded`](./scheduletype-swift.enum/asneeded.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/scheduleddosequantity-7ffhr)*