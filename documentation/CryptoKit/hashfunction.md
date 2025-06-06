# HashFunction

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that performs cryptographically secure hashing.

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
@preconcurrency
protocol HashFunction : Sendable
```

#### Overview

The [`HashFunction`](hashfunction.md) protocol describes an interface for computing a fixed-length digest from an arbitrarily large collection of bytes. Because the digest is small, you can quickly compare the digests to detect a difference in two corresponding data sets. Alternatively, transmit or store data with its digest to detect changes introduced after initially calculating the digest.

Use one of the protocol’s adopters, like [`SHA256`](sha256.md), [`SHA384`](sha384.md), or [`SHA512`](sha512.md), to output a digest whose value varies significantly over even small differences in the input data.

Checking a digest doesn’t guard against changes made by a malicious user who also changes the digest to match. To handle this, compute a message authentication code (MAC) like [`HMAC`](hmac.md) instead. MACs rely on hashing, but incorporate a secret cryptographic key into the digest computation. Only a user that has the key can generate a valid MAC.

## Topics

### Specifying the output type
- [associatedtype Digest : Digest](hashfunction/digest.md)
- [protocol Digest](digest.md)
  A type that represents the output of a hash.
### Computing a hash in one call
- [static func hash<D>(data: D) -> Self.Digest](hashfunction/hash(data:).md)
  Computes the digest of the bytes in the given data instance and returns the computed digest.
### Computing a hash iteratively
- [init()](hashfunction/init.md)
  Creates a hash function.
- [func update<D>(data: D)](hashfunction/update(data:).md)
  Incrementally updates the hash function with the given data.
- [func update(bufferPointer: UnsafeRawBufferPointer)](hashfunction/update(bufferpointer:).md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Self.Digest](hashfunction/finalize.md)
  Finalizes the hash function and returns the computed digest.
### Inspecting hash information
- [static var blockByteCount: Int](hashfunction/blockbytecount.md)
  The number of bytes that represents the hash function’s internal state.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [Insecure.MD5](insecure/md5.md)
- [Insecure.SHA1](insecure/sha1.md)
- [SHA256](sha256.md)
- [SHA384](sha384.md)
- [SHA512](sha512.md)

## See Also

- [struct SHA512](sha512.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.
- [struct SHA384](sha384.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- [struct SHA256](sha256.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction)*