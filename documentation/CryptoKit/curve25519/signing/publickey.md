# Curve25519.Signing.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A Curve25519 public key used to verify cryptographic signatures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](./publickey/init%28rawrepresentation%29.md)
  Creates a Curve25519 public key from a data representation.
### Representing the key
- [var rawRepresentation: Data](./publickey/rawrepresentation.md)
  A representation of the public key.
### Verifying a signature
- [func isValidSignature<S, D>(S, for: D) -> Bool](./publickey/isvalidsignature%28_,for%29.md)
  Verifies an EdDSA signature over Curve25519.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using keys
- [Curve25519.Signing.PrivateKey](./privatekey.md)
  A Curve25519 private key used to create cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey)*