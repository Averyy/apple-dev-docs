# Insecure.MD5Digest

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [static var byteCount: Int](./md5digest/bytecount.md)
  The number of bytes in the digest.
### Describing a digest
- [var description: String](./md5digest/description.md)
  A human-readable description of the digest.
### Hashing a digest
- [func hash(into: inout Hasher)](./md5digest/hash%28into%29.md)
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
- [Insecure.MD5.Digest](./md5/digest.md)
  The digest type for a MD5 hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/md5digest)*