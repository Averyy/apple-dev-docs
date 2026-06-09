# seal(inPlace:using:nonce:authenticating:tag:)

**Framework**: Apple CryptoKit  
**Kind**: method

Secures the given plaintext message with encryption and an optional authentication tag.

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
static func seal(inPlace message: inout MutableRawSpan, using key: SymmetricKey, nonce: AES.GCM.Nonce, authenticating authenticatedData: RawSpan? = nil, tag: inout OutputRawSpan) throws
```

## Parameters

- `message`: The plaintext data to seal, which will be updated in place.
- `key`: A cryptographic key used to seal the message.
- `nonce`: The nonce the sealing process requires.
- `authenticatedData`: Additional data to be authenticated, if provided.
- `tag`: Receives the 16-byte authentication tag


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/seal(inplace:using:nonce:authenticating:tag:))*