# HKFHIRResourceType

**Framework**: HealthKit  
**Kind**: struct

The FHIR resource types supported in HealthKit.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct HKFHIRResourceType
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

## Topics

### Resource Types
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
- [static let medicationRequest: HKFHIRResourceType](hkfhirresourcetype/medicationrequest.md)
  A type that identifies FHIR resources for prescriptions or other orders or requests for medication.
- [static let observation: HKFHIRResourceType](hkfhirresourcetype/observation.md)
  A type that identifies FHIR resources for medical observations, including lab results and vital signs.
- [static let procedure: HKFHIRResourceType](hkfhirresourcetype/procedure.md)
  A type that identifies FHIR resources for procedures performed on the patient.
- [static let coverage: HKFHIRResourceType](hkfhirresourcetype/coverage.md)
  A type that identifies FHIR resources containing information about the user’s insurance coverage.
### Initializers
- [init(rawValue: String)](hkfhirresourcetype/init(rawvalue:).md)
  Returns a new resource type for the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: String](hkfhirresource/identifier.md)
  The value from the FHIR resource’s `id` field.
- [var fhirVersion: HKFHIRVersion](hkfhirresource/fhirversion.md)
  The FHIR version used by this resource.
- [class HKFHIRVersion](hkfhirversion.md)
  The FHIR version.
- [var resourceType: HKFHIRResourceType](hkfhirresource/resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [var sourceURL: URL?](hkfhirresource/sourceurl.md)
  The full URL for the source of the FHIR resource.
- [var data: Data](hkfhirresource/data.md)
  The JSON representation of the FHIR resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresourcetype)*