# UnkeyedEncodingContainer

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.

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
protocol UnkeyedEncodingContainer
```

#### Overview

Encoders should provide types conforming to `UnkeyedEncodingContainer` for their format.

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](./unkeyedencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
- [var count: Int](./unkeyedencodingcontainer/count.md)
  The number of elements encoded into the container.
### Instance Methods
- [func encode(Float) throws](./unkeyedencodingcontainer/encode%28_%29-1rqbg.md)
  Encodes the given value.
- [func encode(Double) throws](./unkeyedencodingcontainer/encode%28_%29-1yl36.md)
  Encodes the given value.
- [func encode(Bool) throws](./unkeyedencodingcontainer/encode%28_%29-24em8.md)
  Encodes the given value.
- [func encode(Int) throws](./unkeyedencodingcontainer/encode%28_%29-30ux3.md)
  Encodes the given value.
- [func encode(UInt) throws](./unkeyedencodingcontainer/encode%28_%29-3dtgb.md)
  Encodes the given value.
- [func encode(UInt128) throws](./unkeyedencodingcontainer/encode%28_%29-4ehqa.md)
  Encodes the given value.
- [func encode(UInt8) throws](./unkeyedencodingcontainer/encode%28_%29-6460j.md)
  Encodes the given value.
- [func encode(Int64) throws](./unkeyedencodingcontainer/encode%28_%29-6jau2.md)
  Encodes the given value.
- [func encode(UInt16) throws](./unkeyedencodingcontainer/encode%28_%29-6moq8.md)
  Encodes the given value.
- [func encode(String) throws](./unkeyedencodingcontainer/encode%28_%29-6o2fd.md)
  Encodes the given value.
- [func encode(Int128) throws](./unkeyedencodingcontainer/encode%28_%29-784h2.md)
  Encodes the given value.
- [func encode(UInt32) throws](./unkeyedencodingcontainer/encode%28_%29-7cs0h.md)
  Encodes the given value.
- [func encode(Int8) throws](./unkeyedencodingcontainer/encode%28_%29-7vq.md)
  Encodes the given value.
- [func encode(Int16) throws](./unkeyedencodingcontainer/encode%28_%29-7za3t.md)
  Encodes the given value.
- [func encode(Int32) throws](./unkeyedencodingcontainer/encode%28_%29-9d3m0.md)
  Encodes the given value.
- [func encode<T>(T) throws](./unkeyedencodingcontainer/encode%28_%29-9k4uf.md)
  Encodes the given value.
- [func encode(UInt64) throws](./unkeyedencodingcontainer/encode%28_%29-9sz81.md)
  Encodes the given value.
- [func encode<T, C>(T, configuration: C.Type) throws](./unkeyedencodingcontainer/encode%28_,configuration%29-3y681.md)
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws](./unkeyedencodingcontainer/encode%28_,configuration%29-85f4v.md)
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-19w8r.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-2bav9.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-36ny.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-3upp3.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-4tdyr.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-54d9i.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-58k1b.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-62wy5.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-7m806.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-862ok.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-89pyf.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-8d3h.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-8vtn5.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-9s06k.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-9sogk.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-kdw8.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](./unkeyedencodingcontainer/encode%28contentsof%29-xykc.md)
  Encodes the elements of the given sequence.
- [func encodeConditional<T>(T) throws](./unkeyedencodingcontainer/encodeconditional%28_%29.md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeNil() throws](./unkeyedencodingcontainer/encodenil%28%29.md)
  Encodes a null value.
- [func encodePredicateExpression<T, each Input>(T, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./unkeyedencodingcontainer/encodepredicateexpression%28_,variable,predicateconfiguration%29-30xlk.md)
- [func encodePredicateExpression<T, each Input>(T, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./unkeyedencodingcontainer/encodepredicateexpression%28_,variable,predicateconfiguration%29-3p9ec.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./unkeyedencodingcontainer/encodepredicateexpressionifpresent%28_,variable,predicateconfiguration%29-438on.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./unkeyedencodingcontainer/encodepredicateexpressionifpresent%28_,variable,predicateconfiguration%29-75j8t.md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type) -> KeyedEncodingContainer<NestedKey>](./unkeyedencodingcontainer/nestedcontainer%28keyedby%29.md)
  Encodes a nested container keyed by the given type and returns it.
- [func nestedUnkeyedContainer() -> any UnkeyedEncodingContainer](./unkeyedencodingcontainer/nestedunkeyedcontainer%28%29.md)
  Encodes an unkeyed encoding container and returns it.
- [func superEncoder() -> any Encoder](./unkeyedencodingcontainer/superencoder%28%29.md)
  Encodes a nested container and returns an `Encoder` instance for encoding `super` into that container.

## See Also

### Encoding Containers
- [protocol SingleValueEncodingContainer](./singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [struct KeyedEncodingContainer](./keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol KeyedEncodingContainerProtocol](./keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer)*