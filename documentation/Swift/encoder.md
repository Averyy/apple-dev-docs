# Encoder

**Framework**: Swift  
**Kind**: protocol

A type that can encode values into a native format for external representation.

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
protocol Encoder
```

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](encoder/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
- [var userInfo: [CodingUserInfoKey : Any]](encoder/userinfo.md)
  Any contextual information set by the user for encoding.
### Instance Methods
- [func container<Key>(keyedBy: Key.Type) -> KeyedEncodingContainer<Key>](encoder/container(keyedby:).md)
  Returns an encoding container appropriate for holding multiple values keyed by the given key type.
- [func singleValueContainer() -> any SingleValueEncodingContainer](encoder/singlevaluecontainer.md)
  Returns an encoding container appropriate for holding a single primitive value.
- [func unkeyedContainer() -> any UnkeyedEncodingContainer](encoder/unkeyedcontainer.md)
  Returns an encoding container appropriate for holding multiple unkeyed values.

## See Also

- [protocol Decoder](decoder.md)
  A type that can decode values from a native format into in-memory representations.
- [enum EncodingError](encodingerror.md)
  An error that occurs during the encoding of a value.
- [enum DecodingError](decodingerror.md)
  An error that occurs during the decoding of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encoder)*