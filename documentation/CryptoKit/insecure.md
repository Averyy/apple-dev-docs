# Insecure

**Framework**: Apple CryptoKit  
**Kind**: enum

A container for older, cryptographically insecure algorithms.

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
enum Insecure
```

#### Overview

> ❗ **Important**: These algorithms aren’t considered cryptographically secure, but the framework provides them for backward compatibility with older services that require them. For new services, avoid these algorithms.

These algorithms aren’t considered cryptographically secure, but the framework provides them for backward compatibility with older services that require them. For new services, avoid these algorithms.

## Topics

### Hashes
- [Insecure.MD5](insecure/md5.md)
  An implementation of MD5 hashing.
- [Insecure.SHA1](insecure/sha1.md)
  An implementation of SHA1 hashing.
### Structures
- [Insecure.MD5Digest](insecure/md5digest.md)
  The output of a MD5 hash.
- [Insecure.SHA1Digest](insecure/sha1digest.md)
  The output of a SHA1 hash.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure)*