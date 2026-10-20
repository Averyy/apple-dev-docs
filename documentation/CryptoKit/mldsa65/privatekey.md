# MLDSA65.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

The private key for MLDSA65.

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
- [init() throws](./privatekey/init%28%29.md)
  Creates a random MLDSA65 private key.
- [init<D>(integrityCheckedRepresentation: D) throws](./privatekey/init%28integritycheckedrepresentation%29.md)
  Initializes a private key from an integrity-checked data representation.
- [init<D>(seedRepresentation: D, publicKey: MLDSA65.PublicKey?) throws](./privatekey/init%28seedrepresentation,publickey%29.md)
  Initializes a private key from the seed representation.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](./privatekey/integritycheckedrepresentation.md)
  The integrity-checked data representation of the private key.
- [var publicKey: MLDSA65.PublicKey](./privatekey/publickey.md)
  The associated public key.
- [var seedRepresentation: Data](./privatekey/seedrepresentation.md)
  The seed representation of the private key.
### Signing data
- [func signature<D>(for: D) throws -> Data](./privatekey/signature%28for%29.md)
  Generates a MLDSA65 signature.
- [func signature<D, C>(for: D, context: C) throws -> Data](./privatekey/signature%28for,context%29.md)
  Generates a MLDSA65 signature, with context.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [MLDSA65.PublicKey](./publickey.md)
  The public key for MLDSA65.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey)*