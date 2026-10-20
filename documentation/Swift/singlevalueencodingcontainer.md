# SingleValueEncodingContainer

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

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
- [var codingPath: [any CodingKey]](./singlevalueencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode(Int) throws](./singlevalueencodingcontainer/encode%28_%29-1mftu.md)
  Encodes a single value of the given type.
- [func encode(Double) throws](./singlevalueencodingcontainer/encode%28_%29-23skf.md)
  Encodes a single value of the given type.
- [func encode(Float) throws](./singlevalueencodingcontainer/encode%28_%29-2c14h.md)
  Encodes a single value of the given type.
- [func encode(Bool) throws](./singlevalueencodingcontainer/encode%28_%29-2oplx.md)
  Encodes a single value of the given type.
- [func encode(UInt64) throws](./singlevalueencodingcontainer/encode%28_%29-39vhy.md)
  Encodes a single value of the given type.
- [func encode(String) throws](./singlevalueencodingcontainer/encode%28_%29-44wsc.md)
  Encodes a single value of the given type.
- [func encode(Int8) throws](./singlevalueencodingcontainer/encode%28_%29-5111.md)
  Encodes a single value of the given type.
- [func encode(Int64) throws](./singlevalueencodingcontainer/encode%28_%29-512uf.md)
  Encodes a single value of the given type.
- [func encode(Int16) throws](./singlevalueencodingcontainer/encode%28_%29-5fuor.md)
  Encodes a single value of the given type.
- [func encode(UInt128) throws](./singlevalueencodingcontainer/encode%28_%29-5kf5u.md)
  Encodes a single value of the given type.
- [func encode(UInt16) throws](./singlevalueencodingcontainer/encode%28_%29-5ndtj.md)
  Encodes a single value of the given type.
- [func encode<T>(T) throws](./singlevalueencodingcontainer/encode%28_%29-687yj.md)
  Encodes a single value of the given type.
- [func encode(UInt32) throws](./singlevalueencodingcontainer/encode%28_%29-6a9w5.md)
  Encodes a single value of the given type.
- [func encode(Int128) throws](./singlevalueencodingcontainer/encode%28_%29-7alir.md)
  Encodes a single value of the given type.
- [func encode(Int32) throws](./singlevalueencodingcontainer/encode%28_%29-9mmv6.md)
  Encodes a single value of the given type.
- [func encode(UInt) throws](./singlevalueencodingcontainer/encode%28_%29-hruu.md)
  Encodes a single value of the given type.
- [func encode(UInt8) throws](./singlevalueencodingcontainer/encode%28_%29-r5hk.md)
  Encodes a single value of the given type.
- [func encodeNil() throws](./singlevalueencodingcontainer/encodenil%28%29.md)
  Encodes a null value.

## See Also

### Encoding Containers
- [struct KeyedEncodingContainer](./keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol KeyedEncodingContainerProtocol](./keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [protocol UnkeyedEncodingContainer](./unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/singlevalueencodingcontainer)*