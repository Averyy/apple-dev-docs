# MLDSA87.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

The public key for MLDSA87.

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
- [init<D>(rawRepresentation: D) throws](mldsa87/publickey/init(rawrepresentation:).md)
  Parses a public key from a serialized representation.
### Getting the raw representation
- [var rawRepresentation: Data](mldsa87/publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Validating a signature
- [func isValidSignature<S, D>(signature: S, for: D) -> Bool](mldsa87/publickey/isvalidsignature(signature:for:).md)
  Verifies a MLDSA87 signature.
- [func isValidSignature<S, D, C>(signature: S, for: D, context: C) -> Bool](mldsa87/publickey/isvalidsignature(signature:for:context:).md)
  Verifies a MLDSA87 signature, in a specific context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLDSA87.PrivateKey](mldsa87/privatekey.md)
  The private key for MLDSA87.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/publickey)*