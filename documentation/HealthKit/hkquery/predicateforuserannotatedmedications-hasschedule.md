# predicateForUserAnnotatedMedications(hasSchedule:)

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
class func predicateForUserAnnotatedMedications(hasSchedule: Bool) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKUserAnnotatedMedicationQuery.

Creates a query predicate that matches HKUserAnnotatedMedication objects that match the schedule status specified.

## Parameters

- `hasSchedule`: The schedule status of the medication. Ex: True will match medications that have a reminders schedule set up in the Health App.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforuserannotatedmedications(hasschedule:))*