# encrypt(inplace:using:nonce:counter:)

**Framework**: Apple CryptoKit  
**Kind**: method

Encrypts the message in-place using unauthenticated ChaCha20.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 1.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func encrypt(inplace message: inout MutableRawSpan, using key: SymmetricKey, nonce: RawSpan, counter: UInt32) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedchacha20/encrypt(inplace:using:nonce:counter:))*