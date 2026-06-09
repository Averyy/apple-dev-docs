# init(copying:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a nonce from the given data.

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
init(copying bytes: RawSpan) throws
```

#### Discussion

Unless your use case calls for a nonce with a specific value, use the [`init()`](aes/gcm/nonce/init().md) method to instead create a random nonce.

## Parameters

- `bytes`: The bytes that represent the nonce. The initializer throws an error if the data has a length smaller than 12 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce/init(copying:))*