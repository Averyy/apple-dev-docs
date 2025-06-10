# signature(for:context:)

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a MLDSA87 signature, with context

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
func signature<D, C>(for data: D, context: C) throws -> Data where D : DataProtocol, C : DataProtocol
```

#### Return Value

The MLDSA87 signature

#### Discussion

> **Note**: If there is a failure producing the signature

## Parameters

- `data`: The data to sign
- `context`: Context for the signature


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa87/privatekey/signature(for:context:))*