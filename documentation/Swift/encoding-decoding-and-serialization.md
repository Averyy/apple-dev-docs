# Encoding, Decoding, and Serialization

**Framework**: Swift

Serialize and deserialize instances of your types with implicit or customized encoding.

## Topics

### Custom Encoding and Decoding
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
- [struct CodingUserInfoKey](codinguserinfokey.md)
  A user-defined key for providing context during encoding and decoding.
### Encoders and Decoders
- [protocol Encoder](encoder.md)
  A type that can encode values into a native format for external representation.
- [protocol Decoder](decoder.md)
  A type that can decode values from a native format into in-memory representations.
- [enum EncodingError](encodingerror.md)
  An error that occurs during the encoding of a value.
- [enum DecodingError](decodingerror.md)
  An error that occurs during the decoding of a value.
### Encoding Containers
- [protocol SingleValueEncodingContainer](singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [struct KeyedEncodingContainer](keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [protocol UnkeyedEncodingContainer](unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.
### Decoding Containers
- [struct KeyedDecodingContainer](keyeddecodingcontainer.md)
  A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [protocol SingleValueDecodingContainer](singlevaluedecodingcontainer.md)
  A container that can support the storage and direct decoding of a single nonkeyed value.
- [protocol KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [protocol UnkeyedDecodingContainer](unkeyeddecodingcontainer.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.

## See Also

- [Basic Behaviors](basic-behaviors.md)
  Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Initialization with Literals](initialization-with-literals.md)
  Allow values of your type to be expressed using different kinds of literals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encoding-decoding-and-serialization)*