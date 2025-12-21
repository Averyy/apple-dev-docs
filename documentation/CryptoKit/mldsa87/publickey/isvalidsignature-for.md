# isValidSignature(_:for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Verifies a MLDSA87 signature.

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
func isValidSignature<S, D>(_ signature: S, for data: D) -> Bool where S : DataProtocol, D : DataProtocol
```

#### Return Value

`true` if the signature is valid, `false` otherwise.

## Parameters

- `signature`: The MLDSA87 signature to verify.
- `data`: The signed data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/publickey/isvalidsignature(_:for:))*