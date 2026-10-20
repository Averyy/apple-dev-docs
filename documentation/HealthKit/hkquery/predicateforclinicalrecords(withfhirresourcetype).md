# predicateForClinicalRecords(withFHIRResourceType:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSPredicate *) predicateForClinicalRecordsWithFHIRResourceType:(HKFHIRResourceType) resourceType;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Creating clinical record predicates
- [class func predicateForClinicalRecords(from: HKSource, fhirResourceType: HKFHIRResourceType, identifier: String) -> NSPredicate](./predicateforclinicalrecords%28from,fhirresourcetype,identifier%29.md)
  Returns a predicate for a specific FHIR resource.
- [class func predicateForVerifiableClinicalRecords(withRelevantDateWithin: DateInterval) -> NSPredicate](./predicateforverifiableclinicalrecords%28withrelevantdatewithin%29.md)
  Returns a predicate that finds verifiable health records with a relevant date within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforclinicalrecords(withfhirresourcetype:))*