# SecureEnclave.MLDSA87.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct PrivateKey
```

## Topics

### Initializers
- [init(accessControl: SecAccessControl) throws](secureenclave/mldsa87/privatekey/init(accesscontrol:).md)
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/mldsa87/privatekey/init(accesscontrol:authenticationcontext:).md)
- [init<D>(dataRepresentation: D) throws](secureenclave/mldsa87/privatekey/init(datarepresentation:).md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](secureenclave/mldsa87/privatekey/init(datarepresentation:authenticationcontext:).md)
### Instance Properties
- [let dataRepresentation: Data](secureenclave/mldsa87/privatekey/datarepresentation.md)
  A data representation of the private key.
- [let publicKey: MLDSA87.PublicKey](secureenclave/mldsa87/privatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func signature<D>(for: D) throws -> Data](secureenclave/mldsa87/privatekey/signature(for:).md)
  Generates a MLDSA87 signature
- [func signature<D, C>(for: D, context: C) throws -> Data](secureenclave/mldsa87/privatekey/signature(for:context:).md)
  Generates a MLDSA87 signature, with context

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa87/privatekey)*