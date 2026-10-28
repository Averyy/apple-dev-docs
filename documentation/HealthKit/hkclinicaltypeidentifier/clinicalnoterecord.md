# clinicalNoteRecord

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A type identifier for records of clinical notes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static let clinicalNoteRecord: HKClinicalTypeIdentifier
```

```c
extern HKClinicalTypeIdentifier const HKClinicalTypeIdentifierClinicalNoteRecord;
```

## Discussion

Clinical notes can have one or more attached files. While these files are often PDFs, HTML, or text files, they can be any format. Check the [`HKAttachment`](../hkattachment.md) object’s [`contentType`](../hkattachment/contenttype.md) property to determine the file type. For more information on accessing the attachments, see [`HKAttachment`](../hkattachment.md).

If your app has permission to read [`clinicalNoteRecord`](./clinicalnoterecord.md) samples, it can also access the attachments. For more information on reading clinical note records, see [Accessing Health Records](../accessing-health-records.md).

## See Also

### Related Documentation
- [class HKClinicalType](../hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [static let documentReference: HKFHIRResourceType](../hkfhirresourcetype/documentreference.md)
  A type that identifies FHIR resources for document references.
- [static let diagnosticReport: HKFHIRResourceType](../hkfhirresourcetype/diagnosticreport.md)
  A type that identifies FHIR resources for findings and interpretation of diagnostic tests.
### Clinical Record Type Identifiers
- [static let allergyRecord: HKClinicalTypeIdentifier](./allergyrecord.md)
  A type identifier for records of allergic or intolerant reactions.
- [static let conditionRecord: HKClinicalTypeIdentifier](./conditionrecord.md)
  A type identifier for records of a condition, problem, diagnosis, or other event.
- [static let immunizationRecord: HKClinicalTypeIdentifier](./immunizationrecord.md)
  A type identifier for records of the current or historical administration of vaccines.
- [static let labResultRecord: HKClinicalTypeIdentifier](./labresultrecord.md)
  A type identifier for records of lab results.
- [static let medicationRecord: HKClinicalTypeIdentifier](./medicationrecord.md)
  A type identifier for records of medication.
- [static let procedureRecord: HKClinicalTypeIdentifier](./procedurerecord.md)
  A type identifier for records of procedures.
- [static let vitalSignRecord: HKClinicalTypeIdentifier](./vitalsignrecord.md)
  A type identifier for records of vital signs.
- [static let coverageRecord: HKClinicalTypeIdentifier](./coveragerecord.md)
  A type identifier for records containing information about the user’s insurance coverage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicaltypeidentifier/clinicalnoterecord)*