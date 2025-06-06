# Accessing Data from a SMART Health Card

**Framework**: Healthkit

Query for and validate a verifiable clinical record.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Xcode 13.3+

#### Overview

> **Note**: This sample code project is associated with WWDC21 session [`10089: Explore Verifiable Health Records`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10089/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

- In Simulator, open Safari, and navigate to `https://spec.smarthealth.cards/examples/`.
- Download one of the SMART Health Cards (like `example-00-e-file.smart-health-card`).
- After the file downloads, tap the download arrow, then select Downloads from the pop-up menu. You can also find the downloaded SMART Health Cards in Files (Browse > On My iPhone > Downloads).
- Select the health card, and follow the instructions to add the card to Health.

## See Also

- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing a User’s Clinical Records](accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
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
- [class HKDocumentSample](hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HealthKit/accessing-data-from-a-smart-health-card)*