# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-384 elliptic curve.

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
func signature<D>(for digest: D) throws -> P384.Signing.ECDSASignature where D : Digest
```

#### Return Value

The signature corresponding to the digest. The signing algorithm employs randomization to generate a different signature on every call, even for the same data and key.

## Parameters

- `digest`: The digest of the data to sign.

## See Also

- [func signature<D>(for: D) throws -> P384.Signing.ECDSASignature](p384/signing/privatekey/signature(for:)-8nncg.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-384 elliptic curve, using SHA-384 as the hash function.
- [P384.Signing.ECDSASignature](p384/signing/ecdsasignature.md)
  A P-384 elliptic curve digital signature algorithm (ECDSA) signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/signature(for:)-wrsj)*