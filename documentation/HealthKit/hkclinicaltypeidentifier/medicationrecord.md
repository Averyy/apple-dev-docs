# medicationRecord

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A type identifier for records of medication.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static let medicationRecord: HKClinicalTypeIdentifier
```

```c
extern HKClinicalTypeIdentifier const HKClinicalTypeIdentifierMedicationRecord;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Related Documentation
- [class HKClinicalType](../hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [static let medicationOrder: HKFHIRResourceType](../hkfhirresourcetype/medicationorder.md)
  A type that identifies FHIR resources for prescriptions or other orders for medication.
- [static let medicationDispense: HKFHIRResourceType](../hkfhirresourcetype/medicationdispense.md)
  A type that identifies FHIR resources for the delivery of medication (usually in response to a prescription).
- [static let medicationStatement: HKFHIRResourceType](../hkfhirresourcetype/medicationstatement.md)
  A type that identifies FHIR resources for statements about medication taken by the patient.
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
- [static let procedureRecord: HKClinicalTypeIdentifier](./procedurerecord.md)
  A type identifier for records of procedures.
- [static let vitalSignRecord: HKClinicalTypeIdentifier](./vitalsignrecord.md)
  A type identifier for records of vital signs.
- [static let coverageRecord: HKClinicalTypeIdentifier](./coveragerecord.md)
  A type identifier for records containing information about the user’s insurance coverage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicaltypeidentifier/medicationrecord)*