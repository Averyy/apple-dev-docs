# SHA256Digest

**Framework**: Apple CryptoKit  
**Kind**: struct

The output of a Secure Hashing Algorithm 2 (SHA-2) hash with a 256-bit digest.

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
struct SHA256Digest
```

## Topics

### Inspecting the digest length
- [static var byteCount: Int](sha256digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](sha256digest/description.md)
  A human-readable description of the digest.
### Hashing a digest
- [func hash(into: inout Hasher)](sha256digest/hash(into:).md)
  Hashes the essential components of the digest by feeding them into the given hash function.

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

## See Also

- [typealias Digest](sha256/digest.md)
  The digest type for a SHA256 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha256digest)*