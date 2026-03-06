# authenticationCode(for:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes a message authentication code for the given data.

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
static func authenticationCode<D>(for data: D, using key: SymmetricKey) -> HMAC<H>.MAC where D : DataProtocol
```

#### Return Value

The message authentication code.

## Parameters

- `data`: The data for which to compute the authentication code.
- `key`: The symmetric key used to secure the computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/authenticationcode(for:using:))*