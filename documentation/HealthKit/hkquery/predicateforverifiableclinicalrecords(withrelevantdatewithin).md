# predicateForVerifiableClinicalRecords(withRelevantDateWithin:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSPredicate *) predicateForVerifiableClinicalRecordsWithRelevantDateWithinDateInterval:(NSDateInterval *) dateInterval;
```

## Discussion

The resulting predicate matches [`HKVerifiableClinicalRecord`](../hkverifiableclinicalrecord.md) instances that have a [`relevantDate`](../hkverifiableclinicalrecord/relevantdate.md) property within the specified date interval.

## Parameters

- `dateInterval`: The start and end date for the predicate.

## See Also

### Creating clinical record predicates
- [class func predicateForClinicalRecords(from: HKSource, fhirResourceType: HKFHIRResourceType, identifier: String) -> NSPredicate](./predicateforclinicalrecords%28from,fhirresourcetype,identifier%29.md)
  Returns a predicate for a specific FHIR resource.
- [class func predicateForClinicalRecords(withFHIRResourceType: HKFHIRResourceType) -> NSPredicate](./predicateforclinicalrecords%28withfhirresourcetype%29.md)
  Returns a predicate for a specific FHIR type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforverifiableclinicalrecords(withrelevantdatewithin:))*