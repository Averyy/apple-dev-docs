# predicateForMedicationDoseEvent(statuses:)

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
class func predicateForMedicationDoseEvent(statuses: Set<NSNumber>) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKQuery subclasses.

Creates a query predicate that matches HKMedicationDoseEvent samples that have any of the statuses specified.

## Parameters

- `statuses`: The logged statuses of the medication dose event to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(statuses:))*