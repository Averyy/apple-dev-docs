# isValidSignature(_:for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-384 elliptic curve.

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
func isValidSignature<D>(_ signature: P384.Signing.ECDSASignature, for digest: D) -> Bool where D : Digest
```

#### Return Value

A Boolean value that’s `true` if the signature is valid for the given digest; otherwise, `false`.

## Parameters

- `signature`: The signature to verify.
- `digest`: The signed digest.

## See Also

- [func isValidSignature<D>(P384.Signing.ECDSASignature, for: D) -> Bool](p384/signing/publickey/isvalidsignature(_:for:)-2zf75.md)
  Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-384 elliptic curve.
- [P384.Signing.ECDSASignature](p384/signing/ecdsasignature.md)
  A P-384 elliptic curve digital signature algorithm (ECDSA) signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/publickey/isvalidsignature(_:for:)-1hrtv)*