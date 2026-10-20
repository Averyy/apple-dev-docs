# KeyedEncodingContainerProtocol

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.

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
protocol KeyedEncodingContainerProtocol
```

#### Overview

Encoders should provide types conforming to `KeyedEncodingContainerProtocol` for their format.

## Topics

### Associated Types
- [associatedtype Key : CodingKey](./keyedencodingcontainerprotocol/key.md)
### Instance Properties
- [var codingPath: [any CodingKey]](./keyedencodingcontainerprotocol/codingpath.md)
  The path of coding keys taken to get to this point in encoding.
### Instance Methods
- [func encode(Int16, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-389ei.md)
  Encodes the given value for the given key.
- [func encode(UInt16, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-44xki.md)
  Encodes the given value for the given key.
- [func encode(Float, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-45mw2.md)
  Encodes the given value for the given key.
- [func encode(UInt64, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-4lg54.md)
  Encodes the given value for the given key.
- [func encode(Bool, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-4xpm2.md)
  Encodes the given value for the given key.
- [func encode(Int, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-53bkq.md)
  Encodes the given value for the given key.
- [func encode(Int128, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-73p1b.md)
  Encodes the given value for the given key.
- [func encode(String, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-74l0h.md)
  Encodes the given value for the given key.
- [func encode(UInt128, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-75dqb.md)
  Encodes the given value for the given key.
- [func encode(Int64, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-7d8l.md)
  Encodes the given value for the given key.
- [func encode(UInt, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-86s3y.md)
  Encodes the given value for the given key.
- [func encode(UInt8, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-887jx.md)
  Encodes the given value for the given key.
- [func encode<T>(T, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-8gl89.md)
  Encodes the given value for the given key.
- [func encode(UInt32, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-8mwtj.md)
  Encodes the given value for the given key.
- [func encode(Double, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-8xq4c.md)
  Encodes the given value for the given key.
- [func encode(Int32, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-9hxpb.md)
  Encodes the given value for the given key.
- [func encode(Int8, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encode%28_,forkey%29-qjna.md)
  Encodes the given value for the given key.
- [func encodeConditional<T>(T, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeconditional%28_,forkey%29.md)
  Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [func encodeIfPresent(UInt8?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-1d9dk.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Float?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-1f6sg.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int8?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-1iqzh.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt64?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-1r22b.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Bool?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-2xq5p.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt128?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-35mgj.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-3j1kl.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-4axra.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int32?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-5ig1w.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int16?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-5uiig.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent<T>(T?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-5xhse.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(String?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-68f89.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Double?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-6xotr.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt16?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-7b7eu.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(UInt32?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-837jy.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int128?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-d7xg.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeIfPresent(Int64?, forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodeifpresent%28_,forkey%29-luij.md)
  Encodes the given value for the given key if it is not `nil`.
- [func encodeNil(forKey: Self.Key) throws](./keyedencodingcontainerprotocol/encodenil%28forkey%29.md)
  Encodes a null value for the given key.
- [func nestedContainer<NestedKey>(keyedBy: NestedKey.Type, forKey: Self.Key) -> KeyedEncodingContainer<NestedKey>](./keyedencodingcontainerprotocol/nestedcontainer%28keyedby,forkey%29.md)
  Stores a keyed encoding container for the given key and returns it.
- [func nestedUnkeyedContainer(forKey: Self.Key) -> any UnkeyedEncodingContainer](./keyedencodingcontainerprotocol/nestedunkeyedcontainer%28forkey%29.md)
  Stores an unkeyed encoding container for the given key and returns it.
- [func superEncoder() -> any Encoder](./keyedencodingcontainerprotocol/superencoder%28%29.md)
  Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [func superEncoder(forKey: Self.Key) -> any Encoder](./keyedencodingcontainerprotocol/superencoder%28forkey%29.md)
  Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

## Relationships

### Conforming Types
- [KeyedEncodingContainer](./keyedencodingcontainer.md)

## See Also

### Encoding Containers
- [protocol SingleValueEncodingContainer](./singlevalueencodingcontainer.md)
  A container that can support the storage and direct encoding of a single non-keyed value.
- [struct KeyedEncodingContainer](./keyedencodingcontainer.md)
  A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [protocol UnkeyedEncodingContainer](./unkeyedencodingcontainer.md)
  A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol)*