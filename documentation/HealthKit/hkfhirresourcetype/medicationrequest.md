# medicationRequest

**Framework**: HealthKit  
**Kind**: property

A type that identifies FHIR resources for prescriptions or other orders or requests for medication.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static let medicationRequest: HKFHIRResourceType
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

#### Discussion

FHIR renamed the resource type for medication requests and orders. FHIR DSTU2 uses the [`medicationOrder`](hkfhirresourcetype/medicationorder.md) resource type, while FHIR R4 uses the [`medicationRequest`](hkfhirresourcetype/medicationrequest.md) resource type.

## See Also

- [static let allergyIntolerance: HKFHIRResourceType](hkfhirresourcetype/allergyintolerance.md)
  A type that identifies FHIR resources for allergies and intolerances.
- [static let condition: HKFHIRResourceType](hkfhirresourcetype/condition.md)
  A type that identifies FHIR resources for a condition, problem, diagnosis, or other event.
- [static let diagnosticReport: HKFHIRResourceType](hkfhirresourcetype/diagnosticreport.md)
  A type that identifies FHIR resources for findings and interpretation of diagnostic tests.
- [static let documentReference: HKFHIRResourceType](hkfhirresourcetype/documentreference.md)
  A type that identifies FHIR resources for document references.
- [static let immunization: HKFHIRResourceType](hkfhirresourcetype/immunization.md)
  A type that identifies FHIR resources for the administration of vaccines.
- [static let medicationOrder: HKFHIRResourceType](hkfhirresourcetype/medicationorder.md)
  A type that identifies FHIR resources for prescriptions or other orders for medication.
- [static let medicationDispense: HKFHIRResourceType](hkfhirresourcetype/medicationdispense.md)
  A type that identifies FHIR resources for the delivery of medication (usually in response to a prescription).
- [static let medicationStatement: HKFHIRResourceType](hkfhirresourcetype/medicationstatement.md)
  A type that identifies FHIR resources for statements about medication taken by the patient.
- [static let observation: HKFHIRResourceType](hkfhirresourcetype/observation.md)
  A type that identifies FHIR resources for medical observations, including lab results and vital signs.
- [static let procedure: HKFHIRResourceType](hkfhirresourcetype/procedure.md)
  A type that identifies FHIR resources for procedures performed on the patient.
- [static let coverage: HKFHIRResourceType](hkfhirresourcetype/coverage.md)
  A type that identifies FHIR resources containing information about the user’s insurance coverage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresourcetype/medicationrequest)*