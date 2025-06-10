# HKVerifiableClinicalRecord

**Framework**: HealthKit  
**Kind**: class

A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKVerifiableClinicalRecord
```

#### Overview

[`HKVerifiableClinicalRecord`](hkverifiableclinicalrecord.md) samples contain data from a SMART Health Card or EU Digital COVID Certificate. Verifiable clinical records combine information about the user’s identity with clinical data, like an immunization record or a lab test result. The organization that produced the data cryptographically signs the bundle.

Apps that use verifiable clinical records can use the cryptographic signature to verify the authenticity of the contents. To verify the card:

1. Access the card’s raw payload using the clinical record’s [`dataRepresentation`](hkverifiableclinicalrecord/datarepresentation.md) property.
2. Unzip the payload and parse out the `iss` value, which contains a URL that identifies the organization that issued the card.
3. Get the public key from the issuer.
4. Verify the payload’s signature.

For more information, see [`SMART Health Cards Framework`](https://developer.apple.comhttps://smarthealth.cards) and [`Electronic Health Certificates`](https://developer.apple.comhttps://github.com/ehn-dcc-development/hcert-spec). You can download example SMART cards for testing and development from [`Examples`](https://developer.apple.comhttps://smarthealth.cards/examples/).

## Topics

### Identifying the Subject
- [var subject: HKVerifiableClinicalRecordSubject](hkverifiableclinicalrecord/subject.md)
  Data about the person whose clinical data the card contains.
### Identifying the Issuer
- [var issuerIdentifier: String](hkverifiableclinicalrecord/issueridentifier.md)
  An identifier that represents the card’s issuer.
### Reading Metadata
- [var issuedDate: Date](hkverifiableclinicalrecord/issueddate.md)
  The date when the issuer created the card.
- [var relevantDate: Date](hkverifiableclinicalrecord/relevantdate.md)
  A date relevant to this record, such as when the issuer administered a vaccine or performed a test.
- [var expirationDate: Date?](hkverifiableclinicalrecord/expirationdate.md)
  The date when the card expires.
- [var recordTypes: [String]](hkverifiableclinicalrecord/recordtypes.md)
  An array of strings representing the types of records contained in the card.
- [var sourceType: HKVerifiableClinicalRecordSourceType?](hkverifiableclinicalrecord/sourcetype.md)
  The source for the verifiable clinical record
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [var itemNames: [String]](hkverifiableclinicalrecord/itemnames.md)
  A human-readable description of the card’s contents.
### Accessing the Raw Payload
- [var dataRepresentation: Data](hkverifiableclinicalrecord/datarepresentation.md)
  A raw representation of the record’s data.
- [var jwsRepresentation: Data](hkverifiableclinicalrecord/jwsrepresentation.md)
  A raw representation of the SMART Health Card’s contents.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class HKFHIRResource](hkfhirresource.md)
  An object containing Fast Healthcare Interoperability Resources (FHIR) data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord)*