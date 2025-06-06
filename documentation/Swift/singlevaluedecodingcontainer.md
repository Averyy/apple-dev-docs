# SingleValueDecodingContainer

**Framework**: Swift  
**Kind**: protocol

A container that can support the storage and direct decoding of a single nonkeyed value.

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
protocol SingleValueDecodingContainer
```

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](singlevaluedecodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func decode(UInt128.Type) throws -> UInt128](singlevaluedecodingcontainer/decode(_:)-1pxe2.md)
  Decodes a single value of the given type.
- [func decode(Int16.Type) throws -> Int16](singlevaluedecodingcontainer/decode(_:)-23u3w.md)
  Decodes a single value of the given type.
- [func decode(Int128.Type) throws -> Int128](singlevaluedecodingcontainer/decode(_:)-2l6ly.md)
  Decodes a single value of the given type.
- [func decode(UInt64.Type) throws -> UInt64](singlevaluedecodingcontainer/decode(_:)-2uokk.md)
  Decodes a single value of the given type.
- [func decode(Int8.Type) throws -> Int8](singlevaluedecodingcontainer/decode(_:)-2vnj6.md)
  Decodes a single value of the given type.
- [func decode<T>(T.Type) throws -> T](singlevaluedecodingcontainer/decode(_:)-3ah76.md)
  Decodes a single value of the given type.
- [func decode(Bool.Type) throws -> Bool](singlevaluedecodingcontainer/decode(_:)-3zbof.md)
  Decodes a single value of the given type.
- [func decode(Int.Type) throws -> Int](singlevaluedecodingcontainer/decode(_:)-4apkx.md)
  Decodes a single value of the given type.
- [func decode(UInt.Type) throws -> UInt](singlevaluedecodingcontainer/decode(_:)-5azw7.md)
  Decodes a single value of the given type.
- [func decode(Int64.Type) throws -> Int64](singlevaluedecodingcontainer/decode(_:)-6aknx.md)
  Decodes a single value of the given type.
- [func decode(UInt8.Type) throws -> UInt8](singlevaluedecodingcontainer/decode(_:)-6wwvl.md)
  Decodes a single value of the given type.
- [func decode(Int32.Type) throws -> Int32](singlevaluedecodingcontainer/decode(_:)-7qn1r.md)
  Decodes a single value of the given type.
- [func decode(String.Type) throws -> String](singlevaluedecodingcontainer/decode(_:)-8f2z9.md)
  Decodes a single value of the given type.
- [func decode(UInt32.Type) throws -> UInt32](singlevaluedecodingcontainer/decode(_:)-8rejh.md)
  Decodes a single value of the given type.
- [func decode(Double.Type) throws -> Double](singlevaluedecodingcontainer/decode(_:)-9wdfz.md)
  Decodes a single value of the given type.
- [func decode(UInt16.Type) throws -> UInt16](singlevaluedecodingcontainer/decode(_:)-vrya.md)
  Decodes a single value of the given type.
- [func decode(Float.Type) throws -> Float](singlevaluedecodingcontainer/decode(_:)-ypkn.md)
  Decodes a single value of the given type.
- [func decodeNil() -> Bool](singlevaluedecodingcontainer/decodenil.md)
  Decodes a null value.

## See Also

- [struct KeyedDecodingContainer](keyeddecodingcontainer.md)
  A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [protocol KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [protocol UnkeyedDecodingContainer](unkeyeddecodingcontainer.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer)*