# signature(for:context:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a MLDSA65 signature, with context

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
func signature<D, C>(for data: D, context: C) throws -> Data where D : DataProtocol, C : DataProtocol
```

#### Return Value

The MLDSA65 signature

#### Discussion

> **Note**: If there is a failure producing the signature

## Parameters

- `data`: The data to sign
- `context`: Context for the signature


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature(for:context:))*