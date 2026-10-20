# Insecure.SHA1Digest

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [static var byteCount: Int](./sha1digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](./sha1digest/description.md)
  A human-readable description of the digest.
### Hasing a digest
- [func hash(into: inout Hasher)](./sha1digest/hash%28into%29.md)
  Hashes the essential components of the digest by feeding them into the given hash function.

## Relationships

### Conforms To
- [ContiguousBytes](../../Foundation/contiguousbytes.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Digest](../digest.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Specifying the output type
- [Insecure.SHA1.Digest](./sha1/digest.md)
  The digest type for a SHA1 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/sha1digest)*