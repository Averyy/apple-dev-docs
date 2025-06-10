# init(ikm:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a Curve25519 private key for key agreement from input keying material.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(ikm: SymmetricKey) throws
```

#### Discussion

This initializer implements the `DeriveKeyPair` algorithm, specified in RFC9180.

## Parameters

- `ikm`: Cryptographic input keying material, which needs to be at least 32 bytes long.

## See Also

- [init()](curve25519/keyagreement/privatekey/init.md)
  Creates a random Curve25519 private key for key agreement.
- [init<D>(rawRepresentation: D) throws](curve25519/keyagreement/privatekey/init(rawrepresentation:).md)
  Creates a Curve25519 private key for key agreement from a collection of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey/init(ikm:))*