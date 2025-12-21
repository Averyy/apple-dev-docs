# predicateForMedicationDoseEvent(scheduledDate:)

**Framework**: HealthKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class func predicateForMedicationDoseEvent(scheduledDate: Date) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKQuery subclasses.

Creates a query predicate that matches HKMedicationDoseEvent samples that have the exact scheduled date specified.

## Parameters

- `scheduledDate`: The exact scheduled date of the medication dose event to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(scheduleddate:))*