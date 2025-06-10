# MLDSA65.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

The private key for MLDSA65.

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

### Creating a private key
- [init() throws](mldsa65/privatekey/init.md)
  Initializes a new random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mldsa65/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked data representation.
- [init<D>(seedRepresentation: D, publicKey: MLDSA65.PublicKey?) throws](mldsa65/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from the seed representation.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](mldsa65/privatekey/integritycheckedrepresentation.md)
  The integrity-checked data representation of the private key.
- [var publicKey: MLDSA65.PublicKey](mldsa65/privatekey/publickey.md)
  The associated public key.
- [var seedRepresentation: Data](mldsa65/privatekey/seedrepresentation.md)
  The seed representation of the private key.
### Signing data
- [func signature<D>(for: D) throws -> Data](mldsa65/privatekey/signature(for:).md)
  Generates a MLDSA65 signature.
- [func signature<D, C>(for: D, context: C) throws -> Data](mldsa65/privatekey/signature(for:context:).md)
  Generates a MLDSA65 signature, with context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLDSA65.PublicKey](mldsa65/publickey.md)
  The public key for MLDSA65.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey)*