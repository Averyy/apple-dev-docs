# Curve25519.Signing.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A Curve25519 private key used to create cryptographic signatures.

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
struct PrivateKey
```

## Topics

### Creating a private key
- [init()](./privatekey/init%28%29.md)
  Creates a random Curve25519 private key for signing.
- [init<D>(rawRepresentation: D) throws](./privatekey/init%28rawrepresentation%29.md)
  Creates a Curve25519 private key for signing from a data representation.
### Reporting the private key
- [var rawRepresentation: Data](./privatekey/rawrepresentation.md)
  The raw representation of the key as a collection of contiguous bytes.
### Finding the public key
- [var publicKey: Curve25519.Signing.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Creating a signature
- [func signature<D>(for: D) throws -> Data](./privatekey/signature%28for%29.md)
  Generates an EdDSA signature over Curve25519.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using keys
- [Curve25519.Signing.PublicKey](./publickey.md)
  A Curve25519 public key used to verify cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey)*