# CodingUserInfoKey

**Framework**: Swift  
**Kind**: struct

A user-defined key for providing context during encoding and decoding.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CodingUserInfoKey
```

## Topics

### Operators
- [static func == (CodingUserInfoKey, CodingUserInfoKey) -> Bool](codinguserinfokey/==(_:_:).md)
  Returns a Boolean value indicating whether the given keys are equal.
### Initializers
- [init?(rawValue: String)](codinguserinfokey/init(rawvalue:).md)
  Creates a new instance with the given raw value.
### Instance Properties
- [var hashValue: Int](codinguserinfokey/hashvalue.md)
  The key’s hash value.
- [let rawValue: String](codinguserinfokey/rawvalue-swift.property.md)
  The key’s string value.
### Instance Methods
- [func hash(into: inout Hasher)](codinguserinfokey/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [CodingUserInfoKey.RawValue](codinguserinfokey/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let actorSystemKey: CodingUserInfoKey](codinguserinfokey/actorsystemkey.md)
  Key which is required to be set on a `Decoder`’s `userInfo` while attempting to `init(from:)` a `DistributedActor`. The stored value under this key must conform to `DistributedActorSystem`.
### Default Implementations
- [Equatable Implementations](codinguserinfokey/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [RawRepresentable](rawrepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [Encoding and Decoding Custom Types](../Foundation/encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [typealias Codable](codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol Encodable](encodable.md)
  A type that can encode itself to an external representation.
- [protocol Decodable](decodable.md)
  A type that can decode itself from an external representation.
- [protocol CodingKey](codingkey.md)
  A type that can be used as a key for encoding and decoding.
- [protocol CodingKeyRepresentable](codingkeyrepresentable.md)
  A type that can be converted to and from a coding key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/codinguserinfokey)*