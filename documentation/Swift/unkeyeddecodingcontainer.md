# UnkeyedDecodingContainer

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.

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
protocol UnkeyedDecodingContainer
```

#### Overview

Decoders should provide types conforming to `UnkeyedDecodingContainer` for their format.

## Topics

### Instance Properties
- [var codingPath: [any CodingKey]](./unkeyeddecodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in decoding.
- [var count: Int?](./unkeyeddecodingcontainer/count.md)
  The number of elements contained within this container.
- [var currentIndex: Int](./unkeyeddecodingcontainer/currentindex.md)
  The current decoding index of the container (i.e. the index of the next element to be decoded.) Incremented after every successful decode call.
- [var isAtEnd: Bool](./unkeyeddecodingcontainer/isatend.md)
  A Boolean value indicating whether there are no more elements left to be decoded in the container.
### Instance Methods
- [func decode(UInt64.Type) throws -> UInt64](./unkeyeddecodingcontainer/decode%28_%29-1jjjp.md)
  Decodes a value of the given type.
- [func decode(Double.Type) throws -> Double](./unkeyeddecodingcontainer/decode%28_%29-276l5.md)
  Decodes a value of the given type.
- [func decode<T>(T.Type) throws -> T](./unkeyeddecodingcontainer/decode%28_%29-2jd5t.md)
  Decodes a value of the given type.
- [func decode(UInt32.Type) throws -> UInt32](./unkeyeddecodingcontainer/decode%28_%29-30psn.md)
  Decodes a value of the given type.
- [func decode(UInt16.Type) throws -> UInt16](./unkeyeddecodingcontainer/decode%28_%29-499mt.md)
  Decodes a value of the given type.
- [func decode(String.Type) throws -> String](./unkeyeddecodingcontainer/decode%28_%29-4cm6k.md)
  Decodes a value of the given type.
- [func decode(Int32.Type) throws -> Int32](./unkeyeddecodingcontainer/decode%28_%29-5eszo.md)
  Decodes a value of the given type.
- [func decode(Int16.Type) throws -> Int16](./unkeyeddecodingcontainer/decode%28_%29-5kbz9.md)
  Decodes a value of the given type.
- [func decode(UInt128.Type) throws -> UInt128](./unkeyeddecodingcontainer/decode%28_%29-66zb4.md)
  Decodes a value of the given type.
- [func decode(Int64.Type) throws -> Int64](./unkeyeddecodingcontainer/decode%28_%29-6o9j1.md)
  Decodes a value of the given type.
- [func decode(UInt.Type) throws -> UInt](./unkeyeddecodingcontainer/decode%28_%29-7gp3y.md)
  Decodes a value of the given type.
- [func decode(Bool.Type) throws -> Bool](./unkeyeddecodingcontainer/decode%28_%29-83ekt.md)
  Decodes a value of the given type.
- [func decode(Int.Type) throws -> Int](./unkeyeddecodingcontainer/decode%28_%29-8g0io.md)
  Decodes a value of the given type.
- [func decode(Int128.Type) throws -> Int128](./unkeyeddecodingcontainer/decode%28_%29-96zc5.md)
  Decodes a value of the given type.
- [func decode(Float.Type) throws -> Float](./unkeyeddecodingcontainer/decode%28_%29-9gfvr.md)
  Decodes a value of the given type.
- [func decode(Int8.Type) throws -> Int8](./unkeyeddecodingcontainer/decode%28_%29-gn40.md)
  Decodes a value of the given type.
- [func decode(UInt8.Type) throws -> UInt8](./unkeyeddecodingcontainer/decode%28_%29-nztw.md)
  Decodes a value of the given type.
- [func decode<T>(T.Type, configuration: T.DecodingConfiguration) throws -> T](./unkeyeddecodingcontainer/decode%28_,configuration%29-3q1ra.md)
- [func decode<T, C>(T.Type, configuration: C.Type) throws -> T](./unkeyeddecodingcontainer/decode%28_,configuration%29-72ctg.md)
- [func decodeIfPresent(Float.Type) throws -> Float?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-1lbyq.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt32.Type) throws -> UInt32?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-1oxo9.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int16.Type) throws -> Int16?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-24deb.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int.Type) throws -> Int?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-2n0nb.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt.Type) throws -> UInt?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-4d6xc.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt8.Type) throws -> UInt8?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-599d9.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int8.Type) throws -> Int8?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-5t8p7.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int64.Type) throws -> Int64?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-62i7k.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt16.Type) throws -> UInt16?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-6aqhk.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int32.Type) throws -> Int32?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-6d53.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt128.Type) throws -> UInt128?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-6j7g9.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Double.Type) throws -> Double?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-6uoka.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(UInt64.Type) throws -> UInt64?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-7dfq.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(String.Type) throws -> String?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-80st4.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Bool.Type) throws -> Bool?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-86f1g.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent(Int128.Type) throws -> Int128?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-gxli.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent<T>(T.Type) throws -> T?](./unkeyeddecodingcontainer/decodeifpresent%28_%29-n5tj.md)
  Decodes a value of the given type, if present.
- [func decodeIfPresent<T, C>(T.Type, configuration: C.Type) throws -> T?](./unkeyeddecodingcontainer/decodeifpresent%28_,configuration%29-3i2jl.md)
- [func decodeIfPresent<T>(T.Type, configuration: T.DecodingConfiguration) throws -> T?](./unkeyeddecodingcontainer/decodeifpresent%28_,configuration%29-7nafo.md)
- [func decodeNil() throws -> Bool](./unkeyeddecodingcontainer/decodenil%28%29.md)
  Decodes a null value.
- [func decodePredicateExpression<each Input, Output>(input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))](./unkeyeddecodingcontainer/decodepredicateexpression%28input,output,predicateconfiguration%29.md)
- [func decodePredicateExpression<each Input>(input: repeat (each Input).Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Bool>, variable: (repeat PredicateExpressions.Variable<each Input>))](./unkeyeddecodingcontainer/decodepredicateexpression%28input,predicateconfiguration%29.md)
- [func decodePredicateExpressionIfPresent<each Input, Output>(input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))?](./unkeyeddecodingcontainer/decodepredicateexpressionifpresent%28input,output,predicateconfiguration%29.md)
- [func decodePredicateExpressionIfPresent<each Input>(input: repeat (each Input).Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Bool>, variable: (repeat PredicateExpressions.Variable<each Input>))?](./unkeyeddecodingcontainer/decodepredicateexpressionifpresent%28input,predicateconfiguration%29.md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type) throws -> KeyedDecodingContainer<NestedKey>](./unkeyeddecodingcontainer/nestedcontainer%28keyedby%29.md)
  Decodes a nested container keyed by the given type.
- [func nestedUnkeyedContainer() throws -> any UnkeyedDecodingContainer](./unkeyeddecodingcontainer/nestedunkeyedcontainer%28%29.md)
  Decodes an unkeyed nested container.
- [func superDecoder() throws -> any Decoder](./unkeyeddecodingcontainer/superdecoder%28%29.md)
  Decodes a nested container and returns a `Decoder` instance for decoding `super` from that container.

## See Also

### Decoding Containers
- [struct KeyedDecodingContainer](./keyeddecodingcontainer.md)
  A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [protocol SingleValueDecodingContainer](./singlevaluedecodingcontainer.md)
  A container that can support the storage and direct decoding of a single nonkeyed value.
- [protocol KeyedDecodingContainerProtocol](./keyeddecodingcontainerprotocol.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer)*