# isValidSignature(_:for:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Instance Method

Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-256 elliptic curve.

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
func isValidSignature<D>(_ signature: P256.Signing.ECDSASignature, for digest: D) -> Bool where D : Digest
```

#### Return Value

A Boolean value that’s `true` if the signature is valid for the given digest; otherwise, `false`.

## Parameters

- `signature`: The signature to verify.
- `digest`: The signed digest.

## See Also

### Verifying a signature
- [func isValidSignature<D>(P256.Signing.ECDSASignature, for: D) -> Bool](./isvalidsignature%28_,for%29-3da2m.md)
  Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-256 elliptic curve.
- [P256.Signing.ECDSASignature](../ecdsasignature.md)
  A P-256 elliptic curve digital signature algorithm (ECDSA) signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing/publickey/isvalidsignature(_:for:)-2rsb5)*