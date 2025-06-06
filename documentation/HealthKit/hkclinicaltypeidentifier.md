# HKClinicalTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

A type identifier for the different categories of clinical records.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
struct HKClinicalTypeIdentifier
```

## Mentions

- [Accessing Health Records](accessing-health-records.md)
- [Authorizing access to health data](authorizing-access-to-health-data.md)

#### Overview

Clinical record samples are read-only, so you can’t request authorization to share clinical record types. You can’t create or save new [`HKClinicalRecord`](hkclinicalrecord.md) objects.

For additional information, see [`Accessing Health Records`](accessing-health-records.md).

## Topics

### Clinical Record Type Identifiers
- [static let allergyRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/allergyrecord.md)
  A type identifier for records of allergic or intolerant reactions.
- [static let clinicalNoteRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/clinicalnoterecord.md)
  A type identifier for records of clinical notes.
- [static let conditionRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/conditionrecord.md)
  A type identifier for records of a condition, problem, diagnosis, or other event.
- [static let immunizationRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/immunizationrecord.md)
  A type identifier for records of the current or historical administration of vaccines.
- [static let labResultRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/labresultrecord.md)
  A type identifier for records of lab results.
- [static let medicationRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/medicationrecord.md)
  A type identifier for records of medication.
- [static let procedureRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/procedurerecord.md)
  A type identifier for records of procedures.
- [static let vitalSignRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/vitalsignrecord.md)
  A type identifier for records of vital signs.
- [static let coverageRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/coveragerecord.md)
  A type identifier for records containing information about the user’s insurance coverage.
### Initializers
- [init(rawValue: String)](hkclinicaltypeidentifier/init(rawvalue:).md)
  Returns a new clinical record type identifier for the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicaltypeidentifier)*