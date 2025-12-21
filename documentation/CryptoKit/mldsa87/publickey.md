# MLDSA87.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

The public key for MLDSA87.

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
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](mldsa87/publickey/init(rawrepresentation:).md)
  Parses a public key from a serialized representation.
### Getting the raw representation
- [var rawRepresentation: Data](mldsa87/publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Instance Methods
- [func isValidSignature<S, D>(S, for: D) -> Bool](mldsa87/publickey/isvalidsignature(_:for:).md)
  Verifies a MLDSA87 signature.
- [func isValidSignature<S, D, C>(S, for: D, context: C) -> Bool](mldsa87/publickey/isvalidsignature(_:for:context:).md)
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