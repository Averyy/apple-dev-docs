# predicateForClinicalRecords(withFHIRResourceType:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for a specific FHIR type.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func predicateForClinicalRecords(withFHIRResourceType resourceType: HKFHIRResourceType) -> NSPredicate
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

## See Also

- [class func predicateForClinicalRecords(from: HKSource, fhirResourceType: HKFHIRResourceType, identifier: String) -> NSPredicate](hkquery/predicateforclinicalrecords(from:fhirresourcetype:identifier:).md)
  Returns a predicate for a specific FHIR resource.
- [class func predicateForVerifiableClinicalRecords(withRelevantDateWithin: DateInterval) -> NSPredicate](hkquery/predicateforverifiableclinicalrecords(withrelevantdatewithin:).md)
  Returns a predicate that finds verifiable health records with a relevant date within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforclinicalrecords(withfhirresourcetype:))*