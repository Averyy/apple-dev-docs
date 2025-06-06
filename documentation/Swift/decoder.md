# Decoder

**Framework**: Swift  
**Kind**: protocol

A type that can decode values from a native format into in-memory representations.

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
protocol Decoder
```

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](decoder/codingpath.md)
  The path of coding keys taken to get to this point in decoding.
- [var userInfo: [CodingUserInfoKey : Any]](decoder/userinfo.md)
  Any contextual information set by the user for decoding.
### Instance Methods
- [func container<Key>(keyedBy: Key.Type) throws -> KeyedDecodingContainer<Key>](decoder/container(keyedby:).md)
  Returns the data stored in this decoder as represented in a container keyed by the given key type.
- [func singleValueContainer() throws -> any SingleValueDecodingContainer](decoder/singlevaluecontainer.md)
  Returns the data stored in this decoder as represented in a container appropriate for holding a single primitive value.
- [func unkeyedContainer() throws -> any UnkeyedDecodingContainer](decoder/unkeyedcontainer.md)
  Returns the data stored in this decoder as represented in a container appropriate for holding values with no keys.

## See Also

- [protocol Encoder](encoder.md)
  A type that can encode values into a native format for external representation.
- [enum EncodingError](encodingerror.md)
  An error that occurs during the encoding of a value.
- [enum DecodingError](decodingerror.md)
  An error that occurs during the decoding of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decoder)*