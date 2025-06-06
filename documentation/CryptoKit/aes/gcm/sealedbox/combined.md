# combined

**Framework**: Apple CryptoKit  
**Kind**: property

A combined element composed of the nonce, encrypted data, and authentication tag.

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
var combined: Data? { get }
```

#### Discussion

The combined representation is only available when the [`AES.GCM.Nonce`](aes/gcm/nonce.md) size is the default size of 12 bytes. The data layout of the combined representation is nonce, ciphertext, then tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/combined)*