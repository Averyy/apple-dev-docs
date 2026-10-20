# ASImportableCredential.CustomFields

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of CustomFields as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CustomFields
```

## Topics

### Initializers
- [init(id: Data?, label: String?, fields: [ASImportableEditableField])](./customfields/init%28id,label,fields%29.md)
### Instance Properties
- [var fields: [ASImportableEditableField]](./customfields/fields.md)
  The collection of fields in this section.
- [var id: Data?](./customfields/id.md)
  Optional: Unique identifier for this section of custom fields.
- [var label: String?](./customfields/label.md)
  Optional: A descriptive title for this section of custom fields.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/customfields)*