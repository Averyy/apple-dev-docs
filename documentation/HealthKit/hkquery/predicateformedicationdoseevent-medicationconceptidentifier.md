# predicateForMedicationDoseEvent(medicationConceptIdentifier:)

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
class func predicateForMedicationDoseEvent(medicationConceptIdentifier: HKHealthConceptIdentifier) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKQuery subclasses.

Creates a query predicate that matches HKMedicationDoseEvent samples that match a medication’s concept identifier.

## Parameters

- `medicationConceptIdentifier`: The identifier of the medication that a dose event was created for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(medicationconceptidentifier:))*