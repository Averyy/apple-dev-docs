# predicateForMedicationDoseEvent(medicationConceptIdentifier:)

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
class func predicateForMedicationDoseEvent(medicationConceptIdentifier: HKHealthConceptIdentifier) -> NSPredicate
```

#### Discussion

Creates a query predicate that matches HKMedicationDoseEvent samples that match a medication’s concept identifier.

## Parameters

- `medicationConceptIdentifier`: The identifier of the medication that a dose event was created for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(medicationconceptidentifier:))*