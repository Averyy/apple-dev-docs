# Token

**Framework**: ManagedSettings  
**Kind**: struct

A representation of an activity, such as an app or website, that doesn’t reveal its identity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Token<T>
```

#### Overview

Managed Settings uses a `Token` to preserve user privacy and prevent anyone outside of a Family Sharing group from identifying what apps and websites the family accesses. You can use tokens to restrict and filter device use without accessing personal information.

The ManagedSettings framework provides the following types of tokens:

## Topics

### Creating a Token
- [init(from: any Decoder) throws](token/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Encoding a Token
- [func encode(to: any Encoder) throws](token/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing Tokens
- [static func == (Token<T>, Token<T>) -> Bool](token/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](token/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [func hash(into: inout Hasher)](token/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](token/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](token/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/token)*