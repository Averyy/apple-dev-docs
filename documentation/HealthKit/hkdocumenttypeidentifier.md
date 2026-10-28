# HKDocumentTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

The identifiers for documents.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct HKDocumentTypeIdentifier
```

```c
typedef NSString * HKDocumentTypeIdentifier;
```

## Overview

To create an [`HKDocumentType`](./hkdocumenttype.md) instance, pass an [`HKDocumentTypeIdentifier`](./hkdocumenttypeidentifier.md) value to the [`documentType(forIdentifier:)`](./hkobjecttype/documenttype%28foridentifier%29.md) method.

For the complete list of quantity type identifiers, see Document Types.

## Topics

### Document Types
- [static let CDA: HKDocumentTypeIdentifier](./hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
### Initializers
- [init(rawValue: String)](./hkdocumenttypeidentifier/init%28rawvalue%29.md)
  Returns a newly initialized document type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating document types
- [class func documentType(forIdentifier: HKDocumentTypeIdentifier) -> HKDocumentType?](./hkobjecttype/documenttype%28foridentifier%29.md)
  Returns the shared document type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifier)*