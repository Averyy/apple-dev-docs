# HKClinicalRecord

**Framework**: HealthKit  
**Kind**: class

A sample that stores a clinical record.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKClinicalRecord
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)

#### Overview

The clinical record stores information about a single condition, procedure, or result. While the record’s properties expose some high-level information, the  [`fhirResource`](hkclinicalrecord/fhirresource.md) property contains the underlying data from the user’s healthcare institution.

Note that the record inherits the [`HKSample`](hksample.md) class’s [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) properties. However, the system does not populate these properties with information from the FHIR data; instead, the [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) reflect the time and date when the system downloaded the FHIR data to the device.

## Topics

### Accessing Clinical Record Data
- [var clinicalType: HKClinicalType](hkclinicalrecord/clinicaltype.md)
  An identifier that indicates the type of record, such as an allergic reaction, a lab result, or a medical procedure.
- [var displayName: String](hkclinicalrecord/displayname.md)
  The primary display name as shown in the Health app.
- [var fhirResource: HKFHIRResource?](hkclinicalrecord/fhirresource.md)
  The Fast Healthcare Interoperability Resources (FHIR) data for this record.

## Relationships

### Inherits From
- [HKSample](hksample.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKClinicalType](hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing a User’s Clinical Records](accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
- [Accessing Data from a SMART Health Card](accessing-data-from-a-smart-health-card.md)
  Query for and validate a verifiable clinical record.
- [class HKFHIRResource](hkfhirresource.md)
  An object containing Fast Healthcare Interoperability Resources (FHIR) data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalrecord)*