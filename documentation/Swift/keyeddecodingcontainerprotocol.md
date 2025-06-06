# KeyedDecodingContainerProtocol

**Framework**: Swift  
**Kind**: protocol

A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.

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
protocol KeyedDecodingContainerProtocol
```

#### Overview

Decoders should provide types conforming to `UnkeyedDecodingContainer` for their format.

## Topics

### Associated Types
- [associatedtype Key : CodingKey](keyeddecodingcontainerprotocol/key.md)
### Instance Properties
- [var allKeys: [Self.Key]](keyeddecodingcontainerprotocol/allkeys.md)
  All the keys the `Decoder` has for this container.
- [var codingPath: [any CodingKey]](keyeddecodingcontainerprotocol/codingpath.md)
  The path of coding keys taken to get to this point in decoding.
### Instance Methods
- [func contains(Self.Key) -> Bool](keyeddecodingcontainerprotocol/contains(_:).md)
  Returns a Boolean value indicating whether the decoder contains a value associated with the given key.
- [func decode(UInt8.Type, forKey: Self.Key) throws -> UInt8](keyeddecodingcontainerprotocol/decode(_:forkey:)-1pd5k.md)
  Decodes a value of the given type for the given key.
- [func decode(Int128.Type, forKey: Self.Key) throws -> Int128](keyeddecodingcontainerprotocol/decode(_:forkey:)-2sa7a.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt32.Type, forKey: Self.Key) throws -> UInt32](keyeddecodingcontainerprotocol/decode(_:forkey:)-3cyg.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt.Type, forKey: Self.Key) throws -> UInt](keyeddecodingcontainerprotocol/decode(_:forkey:)-3zluy.md)
  Decodes a value of the given type for the given key.
- [func decode(Bool.Type, forKey: Self.Key) throws -> Bool](keyeddecodingcontainerprotocol/decode(_:forkey:)-43hen.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt128.Type, forKey: Self.Key) throws -> UInt128](keyeddecodingcontainerprotocol/decode(_:forkey:)-4d1ff.md)
  Decodes a value of the given type for the given key.
- [func decode(Int16.Type, forKey: Self.Key) throws -> Int16](keyeddecodingcontainerprotocol/decode(_:forkey:)-4k53i.md)
  Decodes a value of the given type for the given key.
- [func decode(Int32.Type, forKey: Self.Key) throws -> Int32](keyeddecodingcontainerprotocol/decode(_:forkey:)-5jtvg.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt64.Type, forKey: Self.Key) throws -> UInt64](keyeddecodingcontainerprotocol/decode(_:forkey:)-5kzmf.md)
  Decodes a value of the given type for the given key.
- [func decode(Int.Type, forKey: Self.Key) throws -> Int](keyeddecodingcontainerprotocol/decode(_:forkey:)-62kn6.md)
  Decodes a value of the given type for the given key.
- [func decode(Int64.Type, forKey: Self.Key) throws -> Int64](keyeddecodingcontainerprotocol/decode(_:forkey:)-873gm.md)
  Decodes a value of the given type for the given key.
- [func decode(String.Type, forKey: Self.Key) throws -> String](keyeddecodingcontainerprotocol/decode(_:forkey:)-880hl.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt16.Type, forKey: Self.Key) throws -> UInt16](keyeddecodingcontainerprotocol/decode(_:forkey:)-8h5vd.md)
  Decodes a value of the given type for the given key.
- [func decode(Int8.Type, forKey: Self.Key) throws -> Int8](keyeddecodingcontainerprotocol/decode(_:forkey:)-decq.md)
  Decodes a value of the given type for the given key.
- [func decode(Float.Type, forKey: Self.Key) throws -> Float](keyeddecodingcontainerprotocol/decode(_:forkey:)-kecy.md)
  Decodes a value of the given type for the given key.
- [func decode(Double.Type, forKey: Self.Key) throws -> Double](keyeddecodingcontainerprotocol/decode(_:forkey:)-p613.md)
  Decodes a value of the given type for the given key.
- [func decode<T>(T.Type, forKey: Self.Key) throws -> T](keyeddecodingcontainerprotocol/decode(_:forkey:)-xuqk.md)
  Decodes a value of the given type for the given key.
- [func decodeIfPresent(String.Type, forKey: Self.Key) throws -> String?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-17w89.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int64.Type, forKey: Self.Key) throws -> Int64?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-1qynx.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Double.Type, forKey: Self.Key) throws -> Double?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-1saky.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt16.Type, forKey: Self.Key) throws -> UInt16?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-375xf.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Bool.Type, forKey: Self.Key) throws -> Bool?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-39kc6.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int32.Type, forKey: Self.Key) throws -> Int32?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-3pes5.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt32.Type, forKey: Self.Key) throws -> UInt32?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-5bqjw.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt64.Type, forKey: Self.Key) throws -> UInt64?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-5k5md.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt8.Type, forKey: Self.Key) throws -> UInt8?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-5ymbd.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent<T>(T.Type, forKey: Self.Key) throws -> T?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-6n52q.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt128.Type, forKey: Self.Key) throws -> UInt128?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-6vzzs.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int128.Type, forKey: Self.Key) throws -> Int128?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-7a1da.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int16.Type, forKey: Self.Key) throws -> Int16?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-7jjj2.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int.Type, forKey: Self.Key) throws -> Int?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-7opy8.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int8.Type, forKey: Self.Key) throws -> Int8?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-7p1j1.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Float.Type, forKey: Self.Key) throws -> Float?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-8qp1h.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt.Type, forKey: Self.Key) throws -> UInt?](keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-lc54.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeNil(forKey: Self.Key) throws -> Bool](keyeddecodingcontainerprotocol/decodenil(forkey:).md)
  Decodes a null value for the given key.
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: Self.Key) throws -> KeyedDecodingContainer<NestedKey>](keyeddecodingcontainerprotocol/nestedcontainer(keyedby:forkey:).md)
  Returns the data stored for the given key as represented in a container keyed by the given key type.
- [func nestedUnkeyedContainer(forKey: Self.Key) throws -> any UnkeyedDecodingContainer](keyeddecodingcontainerprotocol/nestedunkeyedcontainer(forkey:).md)
  Returns the data stored for the given key as represented in an unkeyed container.
- [func superDecoder() throws -> any Decoder](keyeddecodingcontainerprotocol/superdecoder.md)
  Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.
- [func superDecoder(forKey: Self.Key) throws -> any Decoder](keyeddecodingcontainerprotocol/superdecoder(forkey:).md)
  Returns a `Decoder` instance for decoding `super` from the container associated with the given key.

## Relationships

### Conforming Types
- [KeyedDecodingContainer](keyeddecodingcontainer.md)

## See Also

- [struct KeyedDecodingContainer](keyeddecodingcontainer.md)
  A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [protocol SingleValueDecodingContainer](singlevaluedecodingcontainer.md)
  A container that can support the storage and direct decoding of a single nonkeyed value.
- [protocol UnkeyedDecodingContainer](unkeyeddecodingcontainer.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol)*