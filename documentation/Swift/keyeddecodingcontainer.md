# KeyedDecodingContainer

**Framework**: Swift  
**Kind**: struct

A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.

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
struct KeyedDecodingContainer<K> where K : CodingKey
```

## Topics

### Initializers
- [init<Container>(Container)](keyeddecodingcontainer/init(_:).md)
  Creates a new instance with the given container.
### Instance Properties
- [var allKeys: [KeyedDecodingContainer<K>.Key]](keyeddecodingcontainer/allkeys.md)
  All the keys the decoder has for this container.
- [var codingPath: [any CodingKey]](keyeddecodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in decoding.
### Instance Methods
- [func contains(KeyedDecodingContainer<K>.Key) -> Bool](keyeddecodingcontainer/contains(_:).md)
  Returns a Boolean value indicating whether the decoder contains a value associated with the given key.
- [func decode(Int32.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int32](keyeddecodingcontainer/decode(_:forkey:)-1d33g.md)
  Decodes a value of the given type for the given key.
- [func decode(Int8.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int8](keyeddecodingcontainer/decode(_:forkey:)-1n3v.md)
  Decodes a value of the given type for the given key.
- [func decode<T>(T.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> T](keyeddecodingcontainer/decode(_:forkey:)-1u4zx.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt32.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt32](keyeddecodingcontainer/decode(_:forkey:)-21ybk.md)
  Decodes a value of the given type for the given key.
- [func decode(Float.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Float](keyeddecodingcontainer/decode(_:forkey:)-3e257.md)
  Decodes a value of the given type for the given key.
- [func decode(String.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> String](keyeddecodingcontainer/decode(_:forkey:)-3egly.md)
  Decodes a value of the given type for the given key.
- [func decode(Int128.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int128](keyeddecodingcontainer/decode(_:forkey:)-3yw73.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt](keyeddecodingcontainer/decode(_:forkey:)-4mzei.md)
  Decodes a value of the given type for the given key.
- [func decode(Int64.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int64](keyeddecodingcontainer/decode(_:forkey:)-5fh1x.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt64.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt64](keyeddecodingcontainer/decode(_:forkey:)-5io1a.md)
  Decodes a value of the given type for the given key.
- [func decode(Double.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Double](keyeddecodingcontainer/decode(_:forkey:)-687gv.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt128.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt128](keyeddecodingcontainer/decode(_:forkey:)-6d98c.md)
  Decodes a value of the given type for the given key.
- [func decode(Int16.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int16](keyeddecodingcontainer/decode(_:forkey:)-721nc.md)
  Decodes a value of the given type for the given key.
- [func decode(Int.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int](keyeddecodingcontainer/decode(_:forkey:)-7vj8e.md)
  Decodes a value of the given type for the given key.
- [func decode(UInt8.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt8](keyeddecodingcontainer/decode(_:forkey:)-8foeb.md)
  Decodes a value of the given type for the given key.
- [func decode<T, C>(CodableConfiguration<T?, C>.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> CodableConfiguration<T?, C>](keyeddecodingcontainer/decode(_:forkey:)-8u7rt.md)
- [func decode(UInt16.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt16](keyeddecodingcontainer/decode(_:forkey:)-9633o.md)
  Decodes a value of the given type for the given key.
- [func decode(Bool.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Bool](keyeddecodingcontainer/decode(_:forkey:)-9fa2u.md)
  Decodes a value of the given type for the given key.
- [func decode<T>(T.Type, forKey: KeyedDecodingContainer<K>.Key, configuration: T.DecodingConfiguration) throws -> T](keyeddecodingcontainer/decode(_:forkey:configuration:)-2rk0t.md)
- [func decode<T, C>(T.Type, forKey: KeyedDecodingContainer<K>.Key, configuration: C.Type) throws -> T](keyeddecodingcontainer/decode(_:forkey:configuration:)-6t8ew.md)
- [func decodeIfPresent(UInt8.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt8?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-1iwt4.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int8.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int8?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-1zmt1.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int64.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int64?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-23pwi.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-2ax45.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent<T>(T.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> T?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-2hn6i.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt128.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt128?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-2thz1.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt64.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt64?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-2yvgn.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Float.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Float?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-3thus.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int32.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int32?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-6zxms.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Bool.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Bool?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-74ir4.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(String.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> String?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-7ucyl.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Double.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Double?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-7x3cg.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt16.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt16?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-85fg3.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int128.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int128?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-897x4.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt32.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt32?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-8tib2.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(Int16.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> Int16?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-91iaz.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent(UInt.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> UInt?](keyeddecodingcontainer/decodeifpresent(_:forkey:)-9fnqb.md)
  Decodes a value of the given type for the given key, if present.
- [func decodeIfPresent<T>(T.Type, forKey: KeyedDecodingContainer<K>.Key, configuration: T.DecodingConfiguration) throws -> T?](keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-469qf.md)
- [func decodeIfPresent<T, C>(T.Type, forKey: KeyedDecodingContainer<K>.Key, configuration: C.Type) throws -> T?](keyeddecodingcontainer/decodeifpresent(_:forkey:configuration:)-5g1cl.md)
- [func decodeNil(forKey: KeyedDecodingContainer<K>.Key) throws -> Bool](keyeddecodingcontainer/decodenil(forkey:).md)
  Decodes a null value for the given key.
- [func decodePredicateExpression<each Input, Output>(forKey: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))](keyeddecodingcontainer/decodepredicateexpression(forkey:input:output:predicateconfiguration:).md)
- [func decodePredicateExpression<each Input>(forKey: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Bool>, variable: (repeat PredicateExpressions.Variable<each Input>))](keyeddecodingcontainer/decodepredicateexpression(forkey:input:predicateconfiguration:).md)
- [func decodePredicateExpressionIfPresent<each Input, Output>(forKey: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))?](keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey:input:output:predicateconfiguration:).md)
- [func decodePredicateExpressionIfPresent<each Input>(forKey: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Bool>, variable: (repeat PredicateExpressions.Variable<each Input>))?](keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey:input:predicateconfiguration:).md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: KeyedDecodingContainer<K>.Key) throws -> KeyedDecodingContainer<NestedKey>](keyeddecodingcontainer/nestedcontainer(keyedby:forkey:).md)
  Returns the data stored for the given key as represented in a container keyed by the given key type.
- [func nestedUnkeyedContainer(forKey: KeyedDecodingContainer<K>.Key) throws -> any UnkeyedDecodingContainer](keyeddecodingcontainer/nestedunkeyedcontainer(forkey:).md)
  Returns the data stored for the given key as represented in an unkeyed container.
- [func superDecoder() throws -> any Decoder](keyeddecodingcontainer/superdecoder.md)
  Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.
- [func superDecoder(forKey: KeyedDecodingContainer<K>.Key) throws -> any Decoder](keyeddecodingcontainer/superdecoder(forkey:).md)
  Returns a `Decoder` instance for decoding `super` from the container associated with the given key.
### Type Aliases
- [KeyedDecodingContainer.Key](keyeddecodingcontainer/key.md)
### Default Implementations
- [KeyedDecodingContainerProtocol Implementations](keyeddecodingcontainer/keyeddecodingcontainerprotocol-implementations.md)

## Relationships

### Conforms To
- [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md)

## See Also

- [protocol SingleValueDecodingContainer](singlevaluedecodingcontainer.md)
  A container that can support the storage and direct decoding of a single nonkeyed value.
- [protocol KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [protocol UnkeyedDecodingContainer](unkeyeddecodingcontainer.md)
  A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainer)*