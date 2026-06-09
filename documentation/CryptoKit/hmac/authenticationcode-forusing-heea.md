# authenticationCode(for:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes a message authentication code for the given data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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