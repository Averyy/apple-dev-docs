# isValidSignature(_:for:context:)

**Framework**: Apple CryptoKit  
**Kind**: method

Verifies a MLDSA65 signature, in a specific context.

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
func isValidSignature<S, D, C>(_ signature: S, for data: D, context: C) -> Bool where S : DataProtocol, D : DataProtocol, C : DataProtocol
```

#### Return Value

`true` if the signature is valid in the specified context, `false` otherwise.

## Parameters

- `signature`: The MLDSA65 signature to verify.
- `data`: The signed data.
- `context`: Context for the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey/isvalidsignature(_:for:context:))*