# MLDSA65.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

The public key for MLDSA65.

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
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](mldsa65/publickey/init(rawrepresentation:).md)
  Parses a public key from a serialized representation.
### Getting the raw representation
- [var rawRepresentation: Data](mldsa65/publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Validating a signature
- [func isValidSignature<S, D>(signature: S, for: D) -> Bool](mldsa65/publickey/isvalidsignature(signature:for:).md)
  Verifies a MLDSA65 signature.
- [func isValidSignature<S, D, C>(signature: S, for: D, context: C) -> Bool](mldsa65/publickey/isvalidsignature(signature:for:context:).md)
  Verifies a MLDSA65 signature, in a specific context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLDSA65.PrivateKey](mldsa65/privatekey.md)
  The private key for MLDSA65.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey)*