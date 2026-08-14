# Insecure.SHA1Digest

**Framework**: Apple CryptoKit  
**Kind**: struct

The output of a SHA1 hash.

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
struct SHA1Digest
```

## Topics

### Inspecting the digest length
- [static var byteCount: Int](insecure/sha1digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](insecure/sha1digest/description.md)
  A human-readable description of the digest.
### Hasing a digest
- [func hash(into: inout Hasher)](insecure/sha1digest/hash(into:).md)
  Hashes the essential components of the digest by feeding them into the given hash function.

## Relationships

### Conforms To
- [ContiguousBytes](../foundation/contiguousbytes.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Digest](digest.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [Insecure.SHA1.Digest](insecure/sha1/digest.md)
  The digest type for a SHA1 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/sha1digest)*