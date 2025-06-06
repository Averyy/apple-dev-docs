# Digest

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the output of a hash.

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
protocol Digest : ContiguousBytes, CustomStringConvertible, Hashable, Sendable, Sequence where Self.Element == UInt8
```

## Topics

### Getting the digest length
- [static var byteCount: Int](digest/bytecount.md)
  The number of bytes in the digest.
### Comparing digests
- [static func == <D>(Self, D) -> Bool](digest/==(_:_:)-7yz3z.md)
  Determines whether a digest is equivalent to a collection of contiguous bytes.
- [static func == (Self, Self) -> Bool](digest/==(_:_:)-6m59k.md)
  Determines whether two digests are equal.
### Default Implementations
- [CustomStringConvertible Implementations](digest/customstringconvertible-implementations.md)

## Relationships

### Inherits From
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)
### Conforming Types
- [Insecure.MD5Digest](insecure/md5digest.md)
- [Insecure.SHA1Digest](insecure/sha1digest.md)
- [SHA256Digest](sha256digest.md)
- [SHA384Digest](sha384digest.md)
- [SHA512Digest](sha512digest.md)

## See Also

- [associatedtype Digest : Digest](hashfunction/digest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/digest)*