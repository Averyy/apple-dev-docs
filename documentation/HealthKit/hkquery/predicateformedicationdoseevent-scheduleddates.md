# predicateForMedicationDoseEvent(scheduledDates:)

**Framework**: HealthKit  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class func predicateForMedicationDoseEvent(scheduledDates: Set<Date>) -> NSPredicate
```

#### Discussion

Creates a query predicate that matches HKMedicationDoseEvent samples that have any of the exact scheduled dates specified.

## Parameters

- `scheduledDates`: The exact scheduled dates of any medication dose event to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(scheduleddates:))*