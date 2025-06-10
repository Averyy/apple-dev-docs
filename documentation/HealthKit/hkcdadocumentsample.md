# HKCDADocumentSample

**Framework**: HealthKit  
**Kind**: class

A Clinical Document Architecture (CDA) sample that stores a single document.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKCDADocumentSample
```

#### Overview

The sample’s `document` property contains an [`HKCDADocument`](hkcdadocument.md) object, representing the underlying XML document.

The [`HKCDADocumentSample`](hkcdadocumentsample.md) class is a concrete subclass of the [`HKDocumentSample`](hkdocumentsample.md) class. Document samples are immutable. HealthKit assigns the document’s properties when the sample is created. They cannot change. If you need to update a document in HealthKit, create a new document sample with the updated CDA document.

## Topics

### Creating CDA Samples
- [convenience init(data: Data, start: Date, end: Date, metadata: [String : Any]?) throws](hkcdadocumentsample/init(data:start:end:metadata:).md)
  Returns a CDA document sample containing the provided XML document and metadata.
- [let HKDetailedCDAValidationErrorKey: String](hkdetailedcdavalidationerrorkey.md)
  A key for accessing validation error information from an error object’s user information dictionary.
### Accessing the Document
- [var document: HKCDADocument?](hkcdadocumentsample/document.md)
  The CDA document.
- [class HKCDADocument](hkcdadocument.md)
  An object representing a Clinical Document Architecture (CDA) document in HealthKit.
### Accessing Validation Errors
- [let HKDetailedCDAValidationErrorKey: String](hkdetailedcdavalidationerrorkey.md)
  A key for accessing validation error information from an error object’s user information dictionary.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathCDAAuthorName: String](hkpredicatekeypathcdaauthorname.md)
  The key path for accessing the author’s name inside a predicate format string.
- [let HKPredicateKeyPathCDACustodianName: String](hkpredicatekeypathcdacustodianname.md)
  The key path for accessing the custodian’s name inside a predicate format string.
- [let HKPredicateKeyPathCDAPatientName: String](hkpredicatekeypathcdapatientname.md)
  The key path for accessing the patient’s name inside a predicate format string.
- [let HKPredicateKeyPathCDATitle: String](hkpredicatekeypathcdatitle.md)
  The key path for accessing the document’s title inside a predicate format string.

## Relationships

### Inherits From
- [HKDocumentSample](hkdocumentsample.md)
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
- [class HKVerifiableClinicalRecord](hkverifiableclinicalrecord.md)
  A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.
- [class HKVerifiableClinicalRecordSubject](hkverifiableclinicalrecordsubject.md)
  The subject associated with a signed clinical record.
- [class HKDocumentSample](hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample)*