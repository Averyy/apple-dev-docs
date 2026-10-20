# SecureEnclave.MLKEM1024.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey](./privatekey/generate%28%29.md)
  Generates a new random private key.
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./privatekey/init%28accesscontrol,authenticationcontext%29.md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](./privatekey/init%28datarepresentation,authenticationcontext%29.md)
### Accessing a key’s properties
- [let dataRepresentation: Data](./privatekey/datarepresentation.md)
  A data representation of the private key.
- [let publicKey: MLKEM1024.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Decapsulating shared secrets
- [func decapsulate<D>(D) throws -> SymmetricKey](./privatekey/decapsulate%28_%29.md)
  Decapsulates the encapsulated shared secret
### Initializers
- [init(accessControl: SecAccessControl) throws](./privatekey/init%28accesscontrol%29.md)
- [init<D>(dataRepresentation: D) throws](./privatekey/init%28datarepresentation%29.md)

## Relationships

### Conforms To
- [KEMPrivateKey](../../kemprivatekey.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey)*