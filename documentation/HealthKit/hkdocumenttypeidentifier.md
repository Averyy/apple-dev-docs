# HKDocumentTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

The identifiers for documents.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKDocumentTypeIdentifier
```

#### Overview

To create an [`HKDocumentType`](hkdocumenttype.md) instance, pass an [`HKDocumentTypeIdentifier`](hkdocumenttypeidentifier.md) value to the [`documentType(forIdentifier:)`](hkobjecttype/documenttype(foridentifier:).md) method.

For the complete list of quantity type identifiers, see Document Types.

## Topics

### Document Types
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
### Initializers
- [init(rawValue: String)](hkdocumenttypeidentifier/init(rawvalue:).md)
  Returns a newly initialized document type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func documentType(forIdentifier: HKDocumentTypeIdentifier) -> HKDocumentType?](hkobjecttype/documenttype(foridentifier:).md)
  Returns the shared document type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifier)*