# open(inPlace:using:nonce:authenticating:tag:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decrypts the message and verifies the authenticity of both the encrypted message and additional data.

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
static func open(inPlace message: inout MutableRawSpan, using key: SymmetricKey, nonce: ChaChaPoly.Nonce, authenticating authenticatedData: RawSpan? = nil, tag: RawSpan) throws
```

#### Discussion

The call throws an error if decryption or authentication fail.

## Parameters

- `message`: The message, which will be decrypted in place.
- `key`: The cryptographic key that was used to seal the message.
- `nonce`: The nonce used to encrypt the message.
- `authenticatedData`: Additional data that was authenticated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/open(inplace:using:nonce:authenticating:tag:))*