# HashedAuthenticationCode

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [var byteCount: Int](./hashedauthenticationcode/bytecount.md)
  The number of bytes in the message authentication code.
### Describing a code
- [var description: String](./hashedauthenticationcode/description.md)
  A human-readable description of the code.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/contiguousbytes.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MessageAuthenticationCode](./messageauthenticationcode.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Working with codes
- [typealias MAC](./hmac/mac.md)
  An alias for a hash-based message authentication code.
- [protocol MessageAuthenticationCode](./messageauthenticationcode.md)
  A type that represents a message authentication code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashedauthenticationcode)*