# predicateForVerifiableClinicalRecords(withRelevantDateWithin:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that finds verifiable health records with a relevant date within the specified range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class func predicateForVerifiableClinicalRecords(withRelevantDateWithin dateInterval: DateInterval) -> NSPredicate
```

#### Discussion

The resulting predicate matches [`HKVerifiableClinicalRecord`](hkverifiableclinicalrecord.md) instances that have a [`relevantDate`](hkverifiableclinicalrecord/relevantdate.md) property within the specified date interval.

## Parameters

- `dateInterval`: The start and end date for the predicate.

## See Also

- [class func predicateForClinicalRecords(from: HKSource, fhirResourceType: HKFHIRResourceType, identifier: String) -> NSPredicate](hkquery/predicateforclinicalrecords(from:fhirresourcetype:identifier:).md)
  Returns a predicate for a specific FHIR resource.
- [class func predicateForClinicalRecords(withFHIRResourceType: HKFHIRResourceType) -> NSPredicate](hkquery/predicateforclinicalrecords(withfhirresourcetype:).md)
  Returns a predicate for a specific FHIR type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforverifiableclinicalrecords(withrelevantdatewithin:))*