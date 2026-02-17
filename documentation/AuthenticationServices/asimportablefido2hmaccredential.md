# ASImportableFIDO2HMACCredential

**Framework**: Authentication Services  
**Kind**: struct

A representation of FIDO2 HMAC Credentials as defined in CXF.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

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
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablefido2hmaccredential)*