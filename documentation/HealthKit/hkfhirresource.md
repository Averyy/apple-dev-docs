# HKFHIRResource

**Framework**: HealthKit  
**Kind**: class

An object containing Fast Healthcare Interoperability Resources (FHIR) data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKFHIRResource
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)

## Topics

### Accessing FHIR Data
- [var identifier: String](hkfhirresource/identifier.md)
  The value from the FHIR resource’s `id` field.
- [var fhirVersion: HKFHIRVersion](hkfhirresource/fhirversion.md)
  The FHIR version used by this resource.
- [class HKFHIRVersion](hkfhirversion.md)
  The FHIR version.
- [var resourceType: HKFHIRResourceType](hkfhirresource/resourcetype.md)
  The value from the FHIR resource’s `resourceType` field.
- [struct HKFHIRResourceType](hkfhirresourcetype.md)
  The FHIR resource types supported in HealthKit.
- [var sourceURL: URL?](hkfhirresource/sourceurl.md)
  The full URL for the source of the FHIR resource.
- [var data: Data](hkfhirresource/data.md)
  The JSON representation of the FHIR resource.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing a User’s Clinical Records](accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
- [Accessing Data from a SMART Health Card](accessing-data-from-a-smart-health-card.md)
  Query for and validate a verifiable clinical record.
- [class HKClinicalRecord](hkclinicalrecord.md)
  A sample that stores a clinical record.
- [class HKVerifiableClinicalRecord](hkverifiableclinicalrecord.md)
  A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.
- [class HKVerifiableClinicalRecordSubject](hkverifiableclinicalrecordsubject.md)
  The subject associated with a signed clinical record.
- [class HKCDADocumentSample](hkcdadocumentsample.md)
  A Clinical Document Architecture (CDA) sample that stores a single document.
- [class HKDocumentSample](hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirresource)*