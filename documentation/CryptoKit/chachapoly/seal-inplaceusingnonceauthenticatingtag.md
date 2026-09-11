# seal(inPlace:using:nonce:authenticating:tag:)

**Framework**: Apple CryptoKit  
**Kind**: method

Secures the given plaintext message in place with encryption and an authentication tag.

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
static func seal(inPlace message: inout MutableRawSpan, using key: SymmetricKey, nonce: ChaChaPoly.Nonce, authenticating authenticatedData: RawSpan? = nil, tag: inout OutputRawSpan) throws
```

## Parameters

- `message`: The plaintext data to seal.
- `key`: A cryptographic key used to seal the message.
- `nonce`: The nonce the sealing process requires.
- `authenticatedData`: Additional data to be authenticated.
- `tag`: Will be updated with the 16-byte authentication tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/seal(inplace:using:nonce:authenticating:tag:))*