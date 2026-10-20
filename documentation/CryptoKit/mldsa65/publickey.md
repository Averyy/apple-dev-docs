# MLDSA65.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

The public key for MLDSA65.

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
- [init<D>(rawRepresentation: D) throws](./publickey/init%28rawrepresentation%29.md)
  Parses a public key from a serialized representation.
### Getting the raw representation
- [var rawRepresentation: Data](./publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Instance Methods
- [func isValidSignature<S, D>(S, for: D) -> Bool](./publickey/isvalidsignature%28_,for%29.md)
  Verifies a MLDSA65 signature.
- [func isValidSignature<S, D, C>(S, for: D, context: C) -> Bool](./publickey/isvalidsignature%28_,for,context%29.md)
  Verifies a MLDSA65 signature, in a specific context.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [MLDSA65.PrivateKey](./privatekey.md)
  The private key for MLDSA65.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey)*