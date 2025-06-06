# UnkeyedEncodingContainer

**Framework**: Swift  
**Kind**: protocol

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
- [var codingPath: [any CodingKey]](unkeyedencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
- [var count: Int](unkeyedencodingcontainer/count.md)
  The number of elements encoded into the container.
### Instance Methods
- [func encode(Float) throws](unkeyedencodingcontainer/encode(_:)-1rqbg.md)
  Encodes the given value.
- [func encode(Double) throws](unkeyedencodingcontainer/encode(_:)-1yl36.md)
  Encodes the given value.
- [func encode(Bool) throws](unkeyedencodingcontainer/encode(_:)-24em8.md)
  Encodes the given value.
- [func encode(Int) throws](unkeyedencodingcontainer/encode(_:)-30ux3.md)
  Encodes the given value.
- [func encode(UInt) throws](unkeyedencodingcontainer/encode(_:)-3dtgb.md)
  Encodes the given value.
- [func encode(UInt128) throws](unkeyedencodingcontainer/encode(_:)-4ehqa.md)
  Encodes the given value.
- [func encode(UInt8) throws](unkeyedencodingcontainer/encode(_:)-6460j.md)
  Encodes the given value.
- [func encode(Int64) throws](unkeyedencodingcontainer/encode(_:)-6jau2.md)
  Encodes the given value.
- [func encode(UInt16) throws](unkeyedencodingcontainer/encode(_:)-6moq8.md)
  Encodes the given value.
- [func encode(String) throws](unkeyedencodingcontainer/encode(_:)-6o2fd.md)
  Encodes the given value.
- [func encode(Int128) throws](unkeyedencodingcontainer/encode(_:)-784h2.md)
  Encodes the given value.
- [func encode(UInt32) throws](unkeyedencodingcontainer/encode(_:)-7cs0h.md)
  Encodes the given value.
- [func encode(Int8) throws](unkeyedencodingcontainer/encode(_:)-7vq.md)
  Encodes the given value.
- [func encode(Int16) throws](unkeyedencodingcontainer/encode(_:)-7za3t.md)
  Encodes the given value.
- [func encode(Int32) throws](unkeyedencodingcontainer/encode(_:)-9d3m0.md)
  Encodes the given value.
- [func encode<T>(T) throws](unkeyedencodingcontainer/encode(_:)-9k4uf.md)
  Encodes the given value.
- [func encode(UInt64) throws](unkeyedencodingcontainer/encode(_:)-9sz81.md)
  Encodes the given value.
- [func encode<T, C>(T, configuration: C.Type) throws](unkeyedencodingcontainer/encode(_:configuration:)-3y681.md)
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws](unkeyedencodingcontainer/encode(_:configuration:)-85f4v.md)
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-19w8r.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-2bav9.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-36ny.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-3upp3.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-4tdyr.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-54d9i.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-58k1b.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-62wy5.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-7m806.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-862ok.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-89pyf.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-8d3h.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-8vtn5.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-9s06k.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-9sogk.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-kdw8.md)
  Encodes the elements of the given sequence.
- [func encode<T>(contentsOf: T) throws](unkeyedencodingcontainer/encode(contentsof:)-xykc.md)
  Encodes the elements of the given sequence.
- [func encodeConditional<T>(T) throws](unkeyedencodingcontainer/encodeconditional(_:).md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeNil() throws](unkeyedencodingcontainer/encodenil.md)
  Encodes a null value.
- [func encodePredicateExpression<T, each Input>(T, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](unkeyedencodingcontainer/encodepredicateexpression(_:variable:predicateconfiguration:)-30xlk.md)
- [func encodePredicateExpression<T, each Input>(T, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](unkeyedencodingcontainer/encodepredicateexpression(_:variable:predicateconfiguration:)-3p9ec.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-438on.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-75j8t.md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type) -> KeyedEncodingContainer<NestedKey>](unkeyedencodingcontainer/nestedcontainer(keyedby:).md)
  Encodes a nested container keyed by the given type and returns it.
- [func nestedUnkeyedContainer() -> any UnkeyedEncodingContainer](unkeyedencodingcontainer/nestedunkeyedcontainer.md)
  Encodes an unkeyed encoding container and returns it.
- [func superEncoder() -> any Encoder](unkeyedencodingcontainer/superencoder.md)
  Encodes a nested container and returns an `Encoder` instance for encoding `super` into that container.

## See Also

- [protocol SingleValueEncodingContainer](singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [struct KeyedEncodingContainer](keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer)*