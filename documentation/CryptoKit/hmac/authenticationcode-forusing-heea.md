# authenticationCode(for:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes a message authentication code for the given data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func authenticationCode(for data: RawSpan, using key: SymmetricKey) -> HMAC<H>.MAC
```

#### Return Value

The message authentication code.

## Parameters

- `data`: The data for which to compute the authentication code.
- `key`: The symmetric key used to secure the computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/authenticationcode(for:using:)-heea)*