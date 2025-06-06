# Codable

**Framework**: Swift  
**Kind**: typealias

A type that can convert itself into and out of an external representation.

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
typealias Codable = Decodable & Encodable
```

#### Discussion

`Codable` is a type alias for the `Encodable` and `Decodable` protocols. When you use `Codable` as a type or a generic constraint, it matches any type that conforms to both protocols.

## See Also

- [Encoding and Decoding Custom Types](../Foundation/encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [protocol Encodable](encodable.md)
  A type that can encode itself to an external representation.
- [protocol Decodable](decodable.md)
  A type that can decode itself from an external representation.
- [protocol CodingKey](codingkey.md)
  A type that can be used as a key for encoding and decoding.
- [protocol CodingKeyRepresentable](codingkeyrepresentable.md)
  A type that can be converted to and from a coding key.
- [struct CodingUserInfoKey](codinguserinfokey.md)
  A user-defined key for providing context during encoding and decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/codable)*