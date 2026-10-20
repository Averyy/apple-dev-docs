# ASImportableCredential.Address

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of Address as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a physical address.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Address
```

## Topics

### Initializers
- [init(streetAddress: ASImportableEditableField?, postalCode: ASImportableEditableField?, city: ASImportableEditableField?, territory: ASImportableEditableField?, country: ASImportableEditableField?, telephone: ASImportableEditableField?)](./address/init%28streetaddress,postalcode,city,territory,country,telephone%29.md)
### Instance Properties
- [var city: ASImportableEditableField?](./address/city.md)
- [var country: ASImportableEditableField?](./address/country.md)
- [var postalCode: ASImportableEditableField?](./address/postalcode.md)
- [var streetAddress: ASImportableEditableField?](./address/streetaddress.md)
- [var telephone: ASImportableEditableField?](./address/telephone.md)
- [var territory: ASImportableEditableField?](./address/territory.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/address)*