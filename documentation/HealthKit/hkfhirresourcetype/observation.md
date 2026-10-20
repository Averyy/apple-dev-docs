# observation

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A type that identifies FHIR resources for medical observations, including lab results and vital signs.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static let observation: HKFHIRResourceType
```

```c
extern HKFHIRResourceType const HKFHIRResourceTypeObservation;
```

## Mentions

- [Accessing Health Records](../accessing-health-records.md)

## See Also

### Related Documentation
- [static let labResultRecord: HKClinicalTypeIdentifier](../hkclinicaltypeidentifier/labresultrecord.md)
  A type identifier for records of lab results.
- [static let vitalSignRecord: HKClinicalTypeIdentifier](../hkclinicaltypeidentifier/vitalsignrecord.md)
  A type identifier for records of vital signs.
### Resource Types
- [static let allergyIntolerance: HKFHIRResourceType](./allergyintolerance.md)
  A type that identifies FHIR resources for allergies and intolerances.
- [static let condition: HKFHIRResourceType](./condition.md)
  A type that identifies FHIR resources for a condition, problem, diagnosis, or other event.
- [static let diagnosticReport: HKFHIRResourceType](./diagnosticreport.md)
  A type that identifies FHIR resources for findings and interpretation of diagnostic tests.
- [static let documentReference: HKFHIRResourceType](./documentreference.md)
  A type that identifies FHIR resources for document references.
- [static let immunization: HKFHIRResourceType](./immunization.md)
  A type that identifies FHIR resources for the administration of vaccines.
- [static let medicationOrder: HKFHIRResourceType](./medicationorder.md)
  A type that identifies FHIR resources for prescriptions or other orders for medication.
- [static let medicationDispense: HKFHIRResourceType](./medicationdispense.md)
  A type that identifies FHIR resources for the delivery of medication (usually in response to a prescription).
- [static let medicationStatement: HKFHIRResourceType](./medicationstatement.md)
  A type that identifies FHIR resources for statements about medication taken by the patient.
- [static let medicationRequest: HKFHIRResourceType](./medicationrequest.md)
  A type that identifies FHIR resources for prescriptions or other orders or requests for medication.
- [static let procedure: HKFHIRResourceType](./procedure.md)
  A type that identifies FHIR resources for procedures performed on the patient.
- [static let coverage: HKFHIRResourceType](./coverage.md)
  A type that identifies FHIR resources containing information about the user’s insurance coverage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresourcetype/observation)*