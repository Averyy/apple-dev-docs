# SecureEnclave.MLKEM1024.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PrivateKey
```

## Topics

### Creating a private key
- [static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey](secureenclave/mlkem1024/privatekey/generate.md)
  Generates a new random private key.
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:).md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](secureenclave/mlkem1024/privatekey/init(datarepresentation:authenticationcontext:).md)
### Accessing a key’s properties
- [let dataRepresentation: Data](secureenclave/mlkem1024/privatekey/datarepresentation.md)
  A data representation of the private key.
- [let publicKey: MLKEM1024.PublicKey](secureenclave/mlkem1024/privatekey/publickey.md)
  The corresponding public key.
### Decapsulating shared secrets
- [func decapsulate<D>(D) throws -> SymmetricKey](secureenclave/mlkem1024/privatekey/decapsulate(_:).md)
  Decapsulates the encapsulated shared secret
### Initializers
- [init(accessControl: SecAccessControl) throws](secureenclave/mlkem1024/privatekey/init(accesscontrol:).md)
- [init<D>(dataRepresentation: D) throws](secureenclave/mlkem1024/privatekey/init(datarepresentation:).md)

## Relationships

### Conforms To
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey)*