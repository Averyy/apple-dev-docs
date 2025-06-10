# HKVerifiableClinicalRecordSourceType

**Framework**: HealthKit  
**Kind**: struct

The source type for the verifiable clinical record.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
struct HKVerifiableClinicalRecordSourceType
```

## Topics

### Identifying Source Types
- [static let euDigitalCOVIDCertificate: HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype/eudigitalcovidcertificate.md)
  A value indicating EU Digital COVID Certificates.
- [static let smartHealthCard: HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype/smarthealthcard.md)
  A value indicating SMART health cards.
### Creating Source Types
- [init(rawValue: String)](hkverifiableclinicalrecordsourcetype/init(rawvalue:).md)
  Creates a source type based on the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HKVerifiableClinicalRecordQueryDescriptor](hkverifiableclinicalrecordquerydescriptor.md)
  A query interface that provides one-time access to a SMART Health Card or EU Digital COVID Certificate using Swift concurrency.
- [class HKVerifiableClinicalRecordQuery](hkverifiableclinicalrecordquery.md)
  A query for one-time access to a SMART Health Card or EU Digital COVID Certificate.
- [struct HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype.md)
  The type of record returned by a verifiable clinical record query.
- [class HKDocumentQuery](hkdocumentquery.md)
  A query that returns a snapshot of all matching documents currently saved in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordsourcetype)*