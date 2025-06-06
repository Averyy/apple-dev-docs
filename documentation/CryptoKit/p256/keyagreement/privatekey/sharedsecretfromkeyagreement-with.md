# sharedSecretFromKeyAgreement(with:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes a shared secret with the provided public key from another party.

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
func sharedSecretFromKeyAgreement(with publicKeyShare: P256.KeyAgreement.PublicKey) throws -> SharedSecret
```

#### Return Value

The computed shared secret.

## Parameters

- `publicKeyShare`: The public key from another party to be combined with the private   key from this user to create the shared secret.

## See Also

- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/privatekey/sharedsecretfromkeyagreement(with:))*