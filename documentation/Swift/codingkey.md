# CodingKey

**Framework**: Swift  
**Kind**: protocol

A type that can be used as a key for encoding and decoding.

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
protocol CodingKey : CustomDebugStringConvertible, CustomStringConvertible, Sendable
```

## Topics

### Initializers
- [init?(intValue: Int)](codingkey/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(stringValue: String)](codingkey/init(stringvalue:).md)
  Creates a new instance from the given string.
### Instance Properties
- [var intValue: Int?](codingkey/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var stringValue: String](codingkey/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).

## Relationships

### Inherits From
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Sendable](sendable.md)

## See Also

- [Encoding and Decoding Custom Types](../Foundation/encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [typealias Codable](codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol Encodable](encodable.md)
  A type that can encode itself to an external representation.
- [protocol Decodable](decodable.md)
  A type that can decode itself from an external representation.
- [protocol CodingKeyRepresentable](codingkeyrepresentable.md)
  A type that can be converted to and from a coding key.
- [struct CodingUserInfoKey](codinguserinfokey.md)
  A user-defined key for providing context during encoding and decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/codingkey)*