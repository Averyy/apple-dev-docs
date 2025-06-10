# Insecure.MD5

**Framework**: Apple CryptoKit  
**Kind**: struct

An implementation of MD5 hashing.

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
struct MD5
```

#### Overview

The [`Insecure.MD5`](insecure/md5.md) hash implements the [`HashFunction`](hashfunction.md) protocol to produce an MD5 digest ([`Insecure.MD5Digest`](insecure/md5digest.md)).

You can compute the digest by calling the static `hash(data:)` method once. Alternatively, if the data that you want to hash is too large to fit in memory, you can compute the digest iteratively by creating a new hash instance, calling the `update(data:)` method repeatedly with blocks of data, and then calling the [`finalize()`](insecure/md5/finalize().md) method to get the result.

> ❗ **Important**: This hash algorithm isn’t considered cryptographically secure, but is provided for backward compatibility with older services that require it. For new services, prefer one of the secure hashes, like [`SHA512`](sha512.md).

## Topics

### Specifying the output type
- [Insecure.MD5.Digest](insecure/md5/digest.md)
  The digest type for a MD5 hash function.
- [Insecure.MD5Digest](insecure/md5digest.md)
  The output of a MD5 hash.
### Reporting the hash length
- [static let byteCount: Int](insecure/md5/bytecount.md)
  The number of bytes in an MD5 digest.
### Computing a hash iteratively
- [init()](insecure/md5/init.md)
  Creates a MD5 hash function.
- [func update(bufferPointer: UnsafeRawBufferPointer)](insecure/md5/update(bufferpointer:).md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Insecure.MD5.Digest](insecure/md5/finalize.md)
  Finalizes the hash function and returns the computed digest.
### Reporting hash function information
- [static let blockByteCount: Int](insecure/md5/blockbytecount.md)
  The number of bytes that represents the hash function’s internal state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HashFunction](hashfunction.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Insecure.SHA1](insecure/sha1.md)
  An implementation of SHA1 hashing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/md5)*