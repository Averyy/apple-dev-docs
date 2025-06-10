# HKDocumentSample

**Framework**: HealthKit  
**Kind**: class

An abstract class that represents a health document in the HealthKit store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HKDocumentSample
```

#### Overview

You should never instantiate an `HKDocumentSample` object directly. Instead, you always work with a concrete subclass. In iOS 10 and watchOS 3, the only concrete class is the [`HKCDADocumentSample`](hkcdadocumentsample.md) class.

Document samples are immutable: You set the sample’s properties when you create it, and they cannot change.

##### Extend Document Samples

Like many HealthKit classes, you should not create any custom subclasses of the `HKDocumentSample` class. You can extend the `HKDocumentSample` class and its subclasses by adding custom metadata keys and values to the metadata dictionary when the object is instantiated.

## Topics

### Accessing the Document Sample Properties
- [var documentType: HKDocumentType](hkdocumentsample/documenttype.md)
  The type of document represented by the sample.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Inherited By
- [HKCDADocumentSample](hkcdadocumentsample.md)
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
- [class HKCDADocumentSample](hkcdadocumentsample.md)
  A Clinical Document Architecture (CDA) sample that stores a single document.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumentsample)*