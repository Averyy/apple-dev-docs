# SHA512Digest

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

The output of a Secure Hashing Algorithm 2 (SHA-2) hash with a 512-bit digest.

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
struct SHA512Digest
```

## Topics

### Inspecting the digest length
- [static var byteCount: Int](./sha512digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](./sha512digest/description.md)
  A human-readable description of the digest.
### Hashing a digest
- [func hash(into: inout Hasher)](./sha512digest/hash%28into%29.md)
  Hashes the essential components of the digest by feeding them into the given hash function.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/contiguousbytes.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Digest](./digest.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Specifying the output type
- [typealias Digest](./sha512/digest.md)
  The digest type for a SHA512 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha512digest)*