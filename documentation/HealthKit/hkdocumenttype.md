# HKDocumentType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A sample type used to create queries for documents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HKDocumentType
```

```objc
@interface HKDocumentType : HKSampleType
```

## Overview

To create a document type instance, use the [`HKObjectType`](./hkobjecttype.md) class’s [`documentType(forIdentifier:)`](./hkobjecttype/documenttype%28foridentifier%29.md) convenience method.

### Subclassing Notes

As with many HealthKit classes, don’t subclass document types.

Additionally, this class reuses the same instance whenever possible. Letting multiple queries share the same document type helps reduce the overall memory usage.

## Topics

### Creating Document Types
- [convenience init(HKDocumentTypeIdentifier)](./hkdocumenttype/init%28_%29.md)
  Creates a document type using the provided identifier.

## Relationships

### Inherits From
- [HKSampleType](./hksampletype.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Medical records
- [Accessing Health Records](./accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](./accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing a User’s Clinical Records](./accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
- [Accessing Data from a SMART Health Card](./accessing-data-from-a-smart-health-card.md)
  Query for and validate a verifiable clinical record.
- [class HKClinicalRecord](./hkclinicalrecord.md)
  A sample that stores a clinical record.
- [class HKFHIRResource](./hkfhirresource.md)
  An object containing Fast Healthcare Interoperability Resources (FHIR) data.
- [class HKVerifiableClinicalRecord](./hkverifiableclinicalrecord.md)
  A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.
- [class HKVerifiableClinicalRecordSubject](./hkverifiableclinicalrecordsubject.md)
  The subject associated with a signed clinical record.
- [class HKCDADocumentSample](./hkcdadocumentsample.md)
  A Clinical Document Architecture (CDA) sample that stores a single document.
- [class HKDocumentSample](./hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](./hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumenttype)*