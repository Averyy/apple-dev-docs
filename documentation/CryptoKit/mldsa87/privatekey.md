# MLDSA87.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

The private key for MLDSA87.

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
  Creates a random MLDSA87 private key.
- [init<D>(integrityCheckedRepresentation: D) throws](./privatekey/init%28integritycheckedrepresentation%29.md)
  Initializes a private key from an integrity-checked data representation.
- [init<D>(seedRepresentation: D, publicKey: MLDSA87.PublicKey?) throws](./privatekey/init%28seedrepresentation,publickey%29.md)
  Initializes a private key from the seed representation.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](./privatekey/integritycheckedrepresentation.md)
  The integrity-checked data representation of the private key.
- [var publicKey: MLDSA87.PublicKey](./privatekey/publickey.md)
  The associated public key.
- [var seedRepresentation: Data](./privatekey/seedrepresentation.md)
  The seed representation of the private key.
### Signing data
- [func signature<D>(for: D) throws -> Data](./privatekey/signature%28for%29.md)
  Generates a MLDSA87 signature.
- [func signature<D, C>(for: D, context: C) throws -> Data](./privatekey/signature%28for,context%29.md)
  Generates a MLDSA87 signature, with context.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [MLDSA87.PublicKey](./publickey.md)
  The public key for MLDSA87.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey)*