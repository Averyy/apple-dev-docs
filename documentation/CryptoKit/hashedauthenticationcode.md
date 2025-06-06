# HashedAuthenticationCode

**Framework**: Apple CryptoKit  
**Kind**: struct

A hash-based message authentication code.

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
struct HashedAuthenticationCode<H> where H : HashFunction
```

## Topics

### Retrieving the code length
- [var byteCount: Int](hashedauthenticationcode/bytecount.md)
  The number of bytes in the message authentication code.
### Describing a code
- [var description: String](hashedauthenticationcode/description.md)
  A human-readable description of the code.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MessageAuthenticationCode](messageauthenticationcode.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [typealias MAC](hmac/mac.md)
  An alias for a hash-based message authentication code.
- [protocol MessageAuthenticationCode](messageauthenticationcode.md)
  A type that represents a message authentication code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashedauthenticationcode)*