# vitalSignRecord

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A type identifier for records of vital signs.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static let vitalSignRecord: HKClinicalTypeIdentifier
```

```c
extern HKClinicalTypeIdentifier const HKClinicalTypeIdentifierVitalSignRecord;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Related Documentation
- [class HKClinicalType](../hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [static let observation: HKFHIRResourceType](../hkfhirresourcetype/observation.md)
  A type that identifies FHIR resources for medical observations, including lab results and vital signs.
### Clinical Record Type Identifiers
- [static let allergyRecord: HKClinicalTypeIdentifier](./allergyrecord.md)
  A type identifier for records of allergic or intolerant reactions.
- [static let clinicalNoteRecord: HKClinicalTypeIdentifier](./clinicalnoterecord.md)
  A type identifier for records of clinical notes.
- [static let conditionRecord: HKClinicalTypeIdentifier](./conditionrecord.md)
  A type identifier for records of a condition, problem, diagnosis, or other event.
- [static let immunizationRecord: HKClinicalTypeIdentifier](./immunizationrecord.md)
  A type identifier for records of the current or historical administration of vaccines.
- [static let labResultRecord: HKClinicalTypeIdentifier](./labresultrecord.md)
  A type identifier for records of lab results.
- [static let medicationRecord: HKClinicalTypeIdentifier](./medicationrecord.md)
  A type identifier for records of medication.
- [static let procedureRecord: HKClinicalTypeIdentifier](./procedurerecord.md)
  A type identifier for records of procedures.
- [static let coverageRecord: HKClinicalTypeIdentifier](./coveragerecord.md)
  A type identifier for records containing information about the user’s insurance coverage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicaltypeidentifier/vitalsignrecord)*