# SingleValueEncodingContainer

**Framework**: Swift  
**Kind**: protocol

A container that can support the storage and direct encoding of a single non-keyed value.

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
protocol SingleValueEncodingContainer
```

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](singlevalueencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode(Int) throws](singlevalueencodingcontainer/encode(_:)-1mftu.md)
  Encodes a single value of the given type.
- [func encode(Double) throws](singlevalueencodingcontainer/encode(_:)-23skf.md)
  Encodes a single value of the given type.
- [func encode(Float) throws](singlevalueencodingcontainer/encode(_:)-2c14h.md)
  Encodes a single value of the given type.
- [func encode(Bool) throws](singlevalueencodingcontainer/encode(_:)-2oplx.md)
  Encodes a single value of the given type.
- [func encode(UInt64) throws](singlevalueencodingcontainer/encode(_:)-39vhy.md)
  Encodes a single value of the given type.
- [func encode(String) throws](singlevalueencodingcontainer/encode(_:)-44wsc.md)
  Encodes a single value of the given type.
- [func encode(Int8) throws](singlevalueencodingcontainer/encode(_:)-5111.md)
  Encodes a single value of the given type.
- [func encode(Int64) throws](singlevalueencodingcontainer/encode(_:)-512uf.md)
  Encodes a single value of the given type.
- [func encode(Int16) throws](singlevalueencodingcontainer/encode(_:)-5fuor.md)
  Encodes a single value of the given type.
- [func encode(UInt128) throws](singlevalueencodingcontainer/encode(_:)-5kf5u.md)
  Encodes a single value of the given type.
- [func encode(UInt16) throws](singlevalueencodingcontainer/encode(_:)-5ndtj.md)
  Encodes a single value of the given type.
- [func encode<T>(T) throws](singlevalueencodingcontainer/encode(_:)-687yj.md)
  Encodes a single value of the given type.
- [func encode(UInt32) throws](singlevalueencodingcontainer/encode(_:)-6a9w5.md)
  Encodes a single value of the given type.
- [func encode(Int128) throws](singlevalueencodingcontainer/encode(_:)-7alir.md)
  Encodes a single value of the given type.
- [func encode(Int32) throws](singlevalueencodingcontainer/encode(_:)-9mmv6.md)
  Encodes a single value of the given type.
- [func encode(UInt) throws](singlevalueencodingcontainer/encode(_:)-hruu.md)
  Encodes a single value of the given type.
- [func encode(UInt8) throws](singlevalueencodingcontainer/encode(_:)-r5hk.md)
  Encodes a single value of the given type.
- [func encodeNil() throws](singlevalueencodingcontainer/encodenil.md)
  Encodes a null value.

## See Also

- [struct KeyedEncodingContainer](keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [protocol UnkeyedEncodingContainer](unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer)*