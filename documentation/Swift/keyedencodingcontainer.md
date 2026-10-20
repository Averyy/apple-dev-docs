# KeyedEncodingContainer

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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
- [init<Container>(Container)](./keyedencodingcontainer/init%28_%29.md)
  Creates a new instance with the given container.
### Instance Properties
- [var codingPath: [any CodingKey]](./keyedencodingcontainer/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode<T, C>(CodableConfiguration<T?, C>, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-11ktw.md)
- [func encode(UInt, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-1m6rk.md)
  Encodes the given value for the given key.
- [func encode<T>(T, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-3a74m.md)
  Encodes the given value for the given key.
- [func encode(UInt8, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-3xzi8.md)
  Encodes the given value for the given key.
- [func encode(Int64, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-4qaju.md)
  Encodes the given value for the given key.
- [func encode(String, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-5bc5p.md)
  Encodes the given value for the given key.
- [func encode(Int, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-78vtz.md)
  Encodes the given value for the given key.
- [func encode(Int128, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-7a0m.md)
  Encodes the given value for the given key.
- [func encode(UInt64, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-7ch7a.md)
  Encodes the given value for the given key.
- [func encode(Int32, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-85f3r.md)
  Encodes the given value for the given key.
- [func encode(Int16, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-8hung.md)
  Encodes the given value for the given key.
- [func encode(UInt16, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-8ik7d.md)
  Encodes the given value for the given key.
- [func encode(UInt128, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-8qhuv.md)
  Encodes the given value for the given key.
- [func encode(Float, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-8y5p6.md)
  Encodes the given value for the given key.
- [func encode(UInt32, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-92a4.md)
  Encodes the given value for the given key.
- [func encode(Int8, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-99z4.md)
  Encodes the given value for the given key.
- [func encode(Double, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-9c512.md)
  Encodes the given value for the given key.
- [func encode(Bool, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encode%28_,forkey%29-9mh8u.md)
  Encodes the given value for the given key.
- [func encode<T, C>(T, forKey: KeyedEncodingContainer<K>.Key, configuration: C.Type) throws](./keyedencodingcontainer/encode%28_,forkey,configuration%29-3i2wq.md)
- [func encode<T>(T, forKey: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws](./keyedencodingcontainer/encode%28_,forkey,configuration%29-4va3q.md)
- [func encodeConditional<T>(T, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeconditional%28_,forkey%29.md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeIfPresent(Int?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-11yvf.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int16?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-250z5.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(String?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-2b1yb.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt16?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-2rzgp.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt32?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-3rw9e.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-45la3.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Float?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-4c8zy.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int32?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-6cflq.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int64?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-70fw4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-70vk4.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt128?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-7c6zc.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Bool?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-7cikn.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int128?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-7wqtl.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt64?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-87bds.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int8?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-9vbxv.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt8?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-9ydxr.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Double?, forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey%29-ikpq.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: KeyedEncodingContainer<K>.Key, configuration: T.EncodingConfiguration) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey,configuration%29-7bzb4.md)
- [func encodeIfPresent<T, C>(T?, forKey: KeyedEncodingContainer<K>.Key, configuration: C.Type) throws](./keyedencodingcontainer/encodeifpresent%28_,forkey,configuration%29-7x1yj.md)
- [func encodeNil(forKey: KeyedEncodingContainer<K>.Key) throws](./keyedencodingcontainer/encodenil%28forkey%29.md)
  Encodes a null value for the given key.
- [func encodePredicateExpression<T, each Input>(T, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./keyedencodingcontainer/encodepredicateexpression%28_,forkey,variable,predicateconfiguration%29-4hhm9.md)
- [func encodePredicateExpression<T, each Input>(T, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./keyedencodingcontainer/encodepredicateexpression%28_,forkey,variable,predicateconfiguration%29-92gv8.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./keyedencodingcontainer/encodepredicateexpressionifpresent%28_,forkey,variable,predicateconfiguration%29-858hy.md)
- [func encodePredicateExpressionIfPresent<T, each Input>(T?, forKey: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws](./keyedencodingcontainer/encodepredicateexpressionifpresent%28_,forkey,variable,predicateconfiguration%29-ivzi.md)
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: KeyedEncodingContainer<K>.Key) -> KeyedEncodingContainer<NestedKey>](./keyedencodingcontainer/nestedcontainer%28keyedby,forkey%29.md)
  Stores a keyed encoding container for the given key and returns it.
- [func nestedUnkeyedContainer(forKey: KeyedEncodingContainer<K>.Key) -> any UnkeyedEncodingContainer](./keyedencodingcontainer/nestedunkeyedcontainer%28forkey%29.md)
  Stores an unkeyed encoding container for the given key and returns it.
- [func superEncoder() -> any Encoder](./keyedencodingcontainer/superencoder%28%29.md)
  Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [func superEncoder(forKey: KeyedEncodingContainer<K>.Key) -> any Encoder](./keyedencodingcontainer/superencoder%28forkey%29.md)
  Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.
### Type Aliases
- [KeyedEncodingContainer.Key](./keyedencodingcontainer/key.md)
### Default Implementations
- [KeyedEncodingContainerProtocol Implementations](./keyedencodingcontainer/keyedencodingcontainerprotocol-implementations.md)

## Relationships

### Conforms To
- [KeyedEncodingContainerProtocol](./keyedencodingcontainerprotocol.md)

## See Also

### Encoding Containers
- [protocol SingleValueEncodingContainer](./singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [protocol KeyedEncodingContainerProtocol](./keyedencodingcontainerprotocol.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [protocol UnkeyedEncodingContainer](./unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer)*