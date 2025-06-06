# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.

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
func signature<D>(for digest: D) throws -> P256.Signing.ECDSASignature where D : Digest
```

#### Return Value

The signature corresponding to the digest. The signing algorithm employs randomization to generate a different signature on every call, even for the same digest and key.

## Parameters

- `digest`: The digest of the data to sign.

## See Also

- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](secureenclave/p256/signing/privatekey/signature(for:)-76j0u.md)
  Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey/signature(for:)-3xogs)*