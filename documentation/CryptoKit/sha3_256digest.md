# SHA3_256Digest

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SHA3_256Digest
```

## Topics

### Instance Properties
- [var description: String](./sha3_256digest/description.md)
  A human-readable description of the digest.
### Instance Methods
- [func hash(into: inout Hasher)](./sha3_256digest/hash%28into%29.md)
  Hashes the essential components of the digest by feeding them into the given hash function.
### Type Properties
- [static var byteCount: Int](./sha3_256digest/bytecount.md)
  The number of bytes in the digest.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_256digest)*