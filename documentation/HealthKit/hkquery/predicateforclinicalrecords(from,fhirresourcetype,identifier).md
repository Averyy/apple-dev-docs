# predicateForClinicalRecords(from:fhirResourceType:identifier:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for a specific FHIR resource.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func predicateForClinicalRecords(from source: HKSource, fhirResourceType resourceType: HKFHIRResourceType, identifier: String) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForClinicalRecordsFromSource:(HKSource *) source FHIRResourceType:(HKFHIRResourceType) resourceType identifier:(NSString *) identifier;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

#### Discussion

The FHIR resource identifier is only unique for a particular resource type from a given source. To uniquely identify a FHIR resource, you must compare the identifier, the resource type, and the source.

## See Also

### Creating clinical record predicates
- [class func predicateForClinicalRecords(withFHIRResourceType: HKFHIRResourceType) -> NSPredicate](./predicateforclinicalrecords%28withfhirresourcetype%29.md)
  Returns a predicate for a specific FHIR type.
- [class func predicateForVerifiableClinicalRecords(withRelevantDateWithin: DateInterval) -> NSPredicate](./predicateforverifiableclinicalrecords%28withrelevantdatewithin%29.md)
  Returns a predicate that finds verifiable health records with a relevant date within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforclinicalrecords(from:fhirresourcetype:identifier:))*