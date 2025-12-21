# signature(for:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a MLDSA65 signature.

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
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

#### Return Value

The MLDSA65 signature. This method throws if CryptoKit encounters an error producing the signature.

## Parameters

- `data`: The data to sign.

## See Also

- [func signature<D, C>(for: D, context: C) throws -> Data](mldsa65/privatekey/signature(for:context:).md)
  Generates a MLDSA65 signature, with context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/signature(for:))*