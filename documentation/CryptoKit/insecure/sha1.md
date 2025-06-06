# Insecure.SHA1

**Framework**: Apple CryptoKit  
**Kind**: struct

An implementation of SHA1 hashing.

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
struct SHA1
```

#### Overview

The [`Insecure.SHA1`](insecure/sha1.md) hash implements the [`HashFunction`](hashfunction.md) protocol to produce a SHA1 digest ([`Insecure.SHA1Digest`](insecure/sha1digest.md)).

You can compute the digest by calling the static `hash(data:)` method once. Alternatively, if the data that you want to hash is too large to fit in memory, you can compute the digest iteratively by creating a new hash instance, calling the `update(data:)` method repeatedly with blocks of data, and then calling the [`finalize()`](insecure/sha1/finalize().md) method to get the result.

> ❗ **Important**: This hash algorithm isn’t considered cryptographically secure, but is provided for backward compatibility with older services that require it. For new services, prefer one of the secure hashes, like [`SHA512`](sha512.md).

This hash algorithm isn’t considered cryptographically secure, but is provided for backward compatibility with older services that require it. For new services, prefer one of the secure hashes, like [`SHA512`](sha512.md).

## Topics

### Specifying the output type
- [Insecure.SHA1.Digest](insecure/sha1/digest.md)
  The digest type for a SHA1 hash function.
- [Insecure.SHA1Digest](insecure/sha1digest.md)
  The output of a SHA1 hash.
### Reporting the hash length
- [static let byteCount: Int](insecure/sha1/bytecount.md)
  The number of bytes in a SHA1 digest.
### Computing a hash iteratively
- [init()](insecure/sha1/init.md)
  Creates a SHA1 hash function.
- [func update(bufferPointer: UnsafeRawBufferPointer)](insecure/sha1/update(bufferpointer:).md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Insecure.SHA1.Digest](insecure/sha1/finalize.md)
  Finalizes the hash function and returns the computed digest.
### Reporting hash function information
- [static let blockByteCount: Int](insecure/sha1/blockbytecount.md)
  The number of bytes that represents the hash function’s internal state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HashFunction](hashfunction.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Insecure.MD5](insecure/md5.md)
  An implementation of MD5 hashing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/sha1)*