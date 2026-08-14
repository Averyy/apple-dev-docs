# ASImportableFIDO2HMACCredential

**Framework**: Authentication Services  
**Kind**: struct

A representation of FIDO2 HMAC Credentials as defined in CXF.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
struct ASImportableFIDO2HMACCredential
```

## Topics

### Initializers
- [init(algorithm: ASImportableFIDO2HMACCredential.Algorithm, credentialWithUV: Data, credentialWithoutUV: Data)](asimportablefido2hmaccredential/init(algorithm:credentialwithuv:credentialwithoutuv:).md)
### Instance Properties
- [var algorithm: ASImportableFIDO2HMACCredential.Algorithm](asimportablefido2hmaccredential/algorithm-swift.property.md)
  Algorithm used to generate the shared secret from the credentials.
- [var credentialWithUV: Data](asimportablefido2hmaccredential/credentialwithuv.md)
  Credential to use when user verification is performed.
- [var credentialWithoutUV: Data](asimportablefido2hmaccredential/credentialwithoutuv.md)
  Credential to use when user verification is not performed.
### Enumerations
- [ASImportableFIDO2HMACCredential.Algorithm](asimportablefido2hmaccredential/algorithm-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablefido2hmaccredential)*