# KeyedEncodingContainer

**Framework**: Swift  
**Kind**: struct

A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.

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
struct KeyedEncodingContainer<K> where K : CodingKey
```

## Topics

### Initializers
- [init<Container>(Container)](keyedencodingcontainer/init(_:).md)
  Creates a new instance with the given container.
### Instance Properties
- [var codingPath: [any CodingKey]](keyedencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode<T, C>(CodableConfiguration<T?, C>, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-11ktw.md)
- [func encode(UInt, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-1m6rk.md)
  Encodes the given value for the given key.
- [func encode<T>(T, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-3a74m.md)
  Encodes the given value for the given key.
- [func encode(UInt8, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-3xzi8.md)
  Encodes the given value for the given key.
- [func encode(Int64, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-4qaju.md)
  Encodes the given value for the given key.
- [func encode(String, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-5bc5p.md)
  Encodes the given value for the given key.
- [func encode(Int, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-78vtz.md)
  Encodes the given value for the given key.
- [func encode(Int128, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-7a0m.md)
  Encodes the given value for the given key.
- [func encode(UInt64, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-7ch7a.md)
  Encodes the given value for the given key.
- [func encode(Int32, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-85f3r.md)
  Encodes the given value for the given key.
- [func encode(Int16, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-8hung.md)
  Encodes the given value for the given key.
- [func encode(UInt16, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-8ik7d.md)
  Encodes the given value for the given key.
- [func encode(UInt128, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-8qhuv.md)
  Encodes the given value for the given key.
- [func encode(Float, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-8y5p6.md)
  Encodes the given value for the given key.
- [func encode(UInt32, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-92a4.md)
  Encodes the given value for the given key.
- [func encode(Int8, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-99z4.md)
  Encodes the given value for the given key.
- [func encode(Double, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-9c512.md)
  Encodes the given value for the given key.
- [func encode(Bool, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encode(_:forkey:)-9mh8u.md)
  Encodes the given value for the given key.
- [func encode<T, C>(T, forKey: KeyedEncodingContainer<K>.Key, configuration: C.Type) throws](keyedencodingcontainer/encode(_:forkey:configuration:)-3i2wq.md)
- [func encode<T>(T, forKey: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws](keyedencodingcontainer/encode(_:forkey:configuration:)-4va3q.md)
- [func encodeConditional<T>(T, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeconditional(_:forkey:).md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeIfPresent(Int?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-11yvf.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int16?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-250z5.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(String?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-2b1yb.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt16?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-2rzgp.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt32?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-3rw9e.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-45la3.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Float?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-4c8zy.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int32?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-6cflq.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int64?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-70fw4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-70vk4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt128?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-7c6zc.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Bool?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-7cikn.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int128?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-7wqtl.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt64?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-87bds.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int8?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-9vbxv.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt8?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-9ydxr.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Double?, forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodeifpresent(_:forkey:)-ikpq.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws](keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7bzb4.md)
- [func encodeIfPresent<T, C>(T?, forKey: KeyedEncodingContainer<K>.Key, configuration: C.Type) throws](keyedencodingcontainer/encodeifpresent(_:forkey:configuration:)-7x1yj.md)
- [func encodeNil(forKey: KeyedEncodingContainer<K>.Key) throws](keyedencodingcontainer/encodenil(forkey:).md)
  Encodes a null value for the given key.
- [func encodePredicateExpression<T, each Input>(T, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](keyedencodingcontainer/encodepredicateexpression(_:forkey:variable:predicateconfiguration:)-4hhm9.md)
- [func encodePredicateExpression<T, each Input>(T, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](keyedencodingcontainer/encodepredicateexpression(_:forkey:variable:predicateconfiguration:)-92gv8.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](keyedencodingcontainer/encodepredicateexpressionifpresent(_:forkey:variable:predicateconfiguration:)-858hy.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](keyedencodingcontainer/encodepredicateexpressionifpresent(_:forkey:variable:predicateconfiguration:)-ivzi.md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: KeyedEncodingContainer<K>.Key) -> KeyedEncodingContainer<NestedKey>](keyedencodingcontainer/nestedcontainer(keyedby:forkey:).md)
  Stores a keyed encoding container for the given key and returns it.
- [func nestedUnkeyedContainer(forKey: KeyedEncodingContainer<K>.Key) -> any UnkeyedEncodingContainer](keyedencodingcontainer/nestedunkeyedcontainer(forkey:).md)
  Stores an unkeyed encoding container for the given key and returns it.
- [func superEncoder() -> any Encoder](keyedencodingcontainer/superencoder.md)
  Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [func superEncoder(forKey: KeyedEncodingContainer<K>.Key) -> any Encoder](keyedencodingcontainer/superencoder(forkey:).md)
  Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.
### Type Aliases
- [KeyedEncodingContainer.Key](keyedencodingcontainer/key.md)
### Default Implementations
- [KeyedEncodingContainerProtocol Implementations](keyedencodingcontainer/keyedencodingcontainerprotocol-implementations.md)

## Relationships

### Conforms To
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)

## See Also

- [protocol SingleValueEncodingContainer](singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [protocol KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [protocol UnkeyedEncodingContainer](unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer)*