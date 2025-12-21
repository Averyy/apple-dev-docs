# predicateForUserAnnotatedMedications(isArchived:)

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
class func predicateForUserAnnotatedMedications(isArchived: Bool) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKUserAnnotatedMedicationQuery.

Creates a query predicate that matches HKUserAnnotatedMedication objects that have the archived status specified.

## Parameters

- `isArchived`: The archived status of the medication. Ex: True will match medications in the archived section in the Health App.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforuserannotatedmedications(isarchived:))*