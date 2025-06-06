# HKVerifiableClinicalRecordCredentialType

**Framework**: HealthKit  
**Kind**: struct

The type of record returned by a verifiable clinical record query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
struct HKVerifiableClinicalRecordCredentialType
```

## Topics

### Identifying Record Types
- [static let covid19: HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype/covid19.md)
  A value that represents records about COVID-19.
- [static let immunization: HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype/immunization.md)
  A value that represents immunizations.
- [static let laboratory: HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype/laboratory.md)
  A value that represents laboratory results.
- [static let recovery: HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype/recovery.md)
  A value that represents recovery information.
### Creating Record Types
- [init(rawValue: String)](hkverifiableclinicalrecordcredentialtype/init(rawvalue:).md)
  Creates a record type based on the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct HKVerifiableClinicalRecordQueryDescriptor](hkverifiableclinicalrecordquerydescriptor.md)
  A query interface that provides one-time access to a SMART Health Card or EU Digital COVID Certificate using Swift concurrency.
- [class HKVerifiableClinicalRecordQuery](hkverifiableclinicalrecordquery.md)
  A query for one-time access to a SMART Health Card or EU Digital COVID Certificate.
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [class HKDocumentQuery](hkdocumentquery.md)
  A query that returns a snapshot of all matching documents currently saved in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordcredentialtype)*