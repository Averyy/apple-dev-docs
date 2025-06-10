# init(_:kem:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates an X-Wing public key for use with HPKE.

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
init<D>(_ serialization: D, kem: HPKE.KEM) throws where D : ContiguousBytes
```

#### Discussion

- serialization: The serialized bytes of the public key.
- kem: The key encapsulation mechanism to use with the public key.

> **Note**: [`HPKE.Errors.inconsistentCiphersuiteAndKey`](hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey/init(_:kem:))*