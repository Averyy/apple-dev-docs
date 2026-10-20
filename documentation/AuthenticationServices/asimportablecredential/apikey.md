# ASImportableCredential.APIKey

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of APIKey as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct APIKey
```

## Topics

### Initializers
- [init(key: ASImportableEditableField?, userName: ASImportableEditableField?, keyType: ASImportableEditableField?, url: ASImportableEditableField?, validFrom: ASImportableEditableField?, expiryDate: ASImportableEditableField?)](./apikey/init%28key,username,keytype,url,validfrom,expirydate%29.md)
### Instance Properties
- [var expiryDate: ASImportableEditableField?](./apikey/expirydate.md)
- [var key: ASImportableEditableField?](./apikey/key.md)
- [var keyType: ASImportableEditableField?](./apikey/keytype.md)
- [var url: ASImportableEditableField?](./apikey/url.md)
- [var userName: ASImportableEditableField?](./apikey/username.md)
  When instantiating from JSON, this property will be populated from the “username” field.
- [var validFrom: ASImportableEditableField?](./apikey/validfrom.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/apikey)*