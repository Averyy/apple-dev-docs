# Insecure.MD5Digest

**Framework**: Apple CryptoKit  
**Kind**: struct

The output of a MD5 hash.

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
struct MD5Digest
```

## Topics

### Inspecting the digest length
- [static var byteCount: Int](insecure/md5digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](insecure/md5digest/description.md)
  A human-readable description of the digest.
### Hashing a digest
- [func hash(into: inout Hasher)](insecure/md5digest/hash(into:).md)
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
- [Sequence](../Swift/Sequence.md)

## See Also

- [Insecure.MD5.Digest](insecure/md5/digest.md)
  The digest type for a MD5 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/md5digest)*