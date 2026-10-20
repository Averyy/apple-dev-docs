# SecureEnclave.MLDSA87.PrivateKey

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

### Initializers
- [init(accessControl: SecAccessControl) throws](./privatekey/init%28accesscontrol%29.md)
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./privatekey/init%28accesscontrol,authenticationcontext%29.md)
- [init<D>(dataRepresentation: D) throws](./privatekey/init%28datarepresentation%29.md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](./privatekey/init%28datarepresentation,authenticationcontext%29.md)
### Instance Properties
- [let dataRepresentation: Data](./privatekey/datarepresentation.md)
  A data representation of the private key.
- [let publicKey: MLDSA87.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func signature<D>(for: D) throws -> Data](./privatekey/signature%28for%29.md)
  Generates a MLDSA87 signature
- [func signature<D, C>(for: D, context: C) throws -> Data](./privatekey/signature%28for,context%29.md)
  Generates a MLDSA87 signature, with context

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa87/privatekey)*