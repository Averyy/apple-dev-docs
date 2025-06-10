# SHA3_256Digest

**Framework**: Apple CryptoKit  
**Kind**: struct

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 2.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct SHA3_256Digest
```

## Topics

### Instance Properties
- [var description: String](sha3_256digest/description.md)
  A human-readable description of the digest.
### Instance Methods
- [func hash(into: inout Hasher)](sha3_256digest/hash(into:).md)
  Hashes the essential components of the digest by feeding them into the given hash function.
### Type Properties
- [static var byteCount: Int](sha3_256digest/bytecount.md)
  The number of bytes in the digest.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Digest](digest.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_256digest)*