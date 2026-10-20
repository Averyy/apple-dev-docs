# ASImportableCredential.SSHKey

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

A representation of SSHKey as defined in the [Credential Exchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct SSHKey
```

## Topics

### Initializers
- [init(keyType: String, privateKey: Data, keyComment: String?, creationDate: ASImportableEditableField?, expiryDate: ASImportableEditableField?, keyGenerationSource: ASImportableEditableField?)](./sshkey/init%28keytype,privatekey,keycomment,creationdate,expirydate,keygenerationsource%29.md)
### Instance Properties
- [var creationDate: ASImportableEditableField?](./sshkey/creationdate.md)
- [var expiryDate: ASImportableEditableField?](./sshkey/expirydate.md)
- [var keyComment: String?](./sshkey/keycomment.md)
- [var keyGenerationSource: ASImportableEditableField?](./sshkey/keygenerationsource.md)
- [var keyType: String](./sshkey/keytype.md)
- [var privateKey: Data](./sshkey/privatekey.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/sshkey)*