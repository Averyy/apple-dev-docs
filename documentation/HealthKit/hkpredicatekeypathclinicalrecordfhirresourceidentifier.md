# HKPredicateKeyPathClinicalRecordFHIRResourceIdentifier

**Framework**: HealthKit  
**Kind**: var

The key path for accessing the clinical record’s Fast Healthcare Interoperability Resources (FHIR) identifier.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let HKPredicateKeyPathClinicalRecordFHIRResourceIdentifier: String
```

#### Discussion

The FHIR resource identifier is only unique for a particular resource type from a given source. To uniquely identify a FHIR resource, you must compare the identifier, the resource type, and the source.

## See Also

- [let HKPredicateKeyPathClinicalRecordFHIRResourceType: String](hkpredicatekeypathclinicalrecordfhirresourcetype.md)
  The key path for accessing the resource type of a Fast Healthcare Interoperability Resources (FHIR) record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathclinicalrecordfhirresourceidentifier)*