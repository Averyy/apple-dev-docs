# Insecure.UnauthenticatedChaCha20

**Framework**: Apple CryptoKit  
**Kind**: struct

Unauthenticated ChaCha20 stream cipher.

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
struct UnauthenticatedChaCha20
```

#### Overview

> ⚠️ **Warning**: This cipher provides no authentication or integrity checking. Only use this when a higher-level protocol provides its own integrity and confidentiality guarantees, or in higher-level protocols that have received security analysis (such as QUIC header protection, RFC9001).

## Topics

### Type Methods
- [static func encrypt(inplace: inout MutableRawSpan, using: SymmetricKey, nonce: RawSpan, counter: UInt32) throws](insecure/unauthenticatedchacha20/encrypt(inplace:using:nonce:counter:).md)
  Encrypts the message in-place using unauthenticated ChaCha20.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedchacha20)*