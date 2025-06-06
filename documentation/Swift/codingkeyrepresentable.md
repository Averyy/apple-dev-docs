# CodingKeyRepresentable

**Framework**: Swift  
**Kind**: protocol

A type that can be converted to and from a coding key.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
protocol CodingKeyRepresentable
```

#### Overview

With a `CodingKeyRepresentable` type, you can losslessly convert between a custom type and a `CodingKey` type.

Conforming a type to `CodingKeyRepresentable` lets you opt in to encoding and decoding `Dictionary` values keyed by the conforming type to and from a keyed container, rather than encoding and decoding the dictionary as an unkeyed container of alternating key-value pairs.

## Topics

### Initializers
- [init?<T>(codingKey: T)](codingkeyrepresentable/init(codingkey:).md)
### Instance Properties
- [var codingKey: any CodingKey](codingkeyrepresentable/codingkey.md)

## Relationships

### Conforming Types
- [Int](int.md)
- [String](string.md)

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
- [struct CodingUserInfoKey](codinguserinfokey.md)
  A user-defined key for providing context during encoding and decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/codingkeyrepresentable)*