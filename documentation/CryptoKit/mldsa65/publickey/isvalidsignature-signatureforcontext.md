# isValidSignature(signature:for:context:)

**Framework**: Apple CryptoKit  
**Kind**: method

Verifies a MLDSA65 signature, in a specific context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func isValidSignature<S, D, C>(signature: S, for data: D, context: C) -> Bool where S : DataProtocol, D : DataProtocol, C : DataProtocol
```

#### Return Value

`true` if the signature is valid in the specified context, `false` otherwise.

## Parameters

- `signature`: The MLDSA65 signature to verify.
- `data`: The signed data.
- `context`: Context for the signature.

## See Also

- [func isValidSignature<S, D>(signature: S, for: D) -> Bool](mldsa65/publickey/isvalidsignature(signature:for:).md)
  Verifies a MLDSA65 signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey/isvalidsignature(signature:for:context:))*